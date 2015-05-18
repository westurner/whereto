
==========
Roadmap
==========

Models
*******


::

    @prefix ex: <https://westurner.org/whereto/ns/ex#> ;
    @prefix tags: <https://westurner.org/whereto/ns/tags#> ;

    tags:Tag a schema:Thing ;
        schema:name "tag"@en ;
        .

    tags:tag a rdfs:Property ;
        schema:name "tag"@en ;
        .

    //

    tags:todo a tags:Tag ;
        schema:name "todo"@en ;
        .

    tags:ready a tags:Tag ;
        schema:name "ready"@en ;
        .

    tags:in_progress a tags:Tag ;
        schema:name "in progress"@en ;
        .

    tags:done a tags:Tag ;
        schema:name "done"@en ;
        .

    //

    tags:interested a tags:Tag ;
        schema:name "interested"@en ;
        .

    tags:acquiring a tags:Tag ;
        schema:name "renting"@en ;
        .

    tags:leasing a tags:Tag ;
        schema:name "leasing"@en ;
        .

    tags:renting_out a tags:Tag ;
        schema:name "renting out"@en ;
        .

    tags:leasing_out a tags:Tag ;
        schema:name "leasing out"@en ;
        .

    tags:own a tags:Tag ;
        schema:name "own"@en ;
        .


    ////

    ex:Message a schema:Thing ;
    //    schema:name
    //    schema:desc
    //    ex:parsedTags
        .

    ex:Todo a schema:Thing ;
    //  schema:name
    //  schema:desc *
    //  tags:tags
    //  ex:todoState [todo|ready|in progress|done]
        .

    ex:Property a schema:Thing ;
    //  schema:name
    //  schema:desc
    //  tags:tag
    //  ex:propertyState
        .

    ex:Project a schema:Thing ;
    // schema:name
    // schema:desc
    // tags:tag
    // ex:projectState
        .

    ex:PropertyProject subclassof ex:Project
    // schema:name
    // schema:desc
    // properties = { }
        .

    ex:todoState a rdfs:Property ;
        rdfs:range tags:Tag ;
        //  rdfs:range tags:Tag { todo|ready|in progress|done }
        .

    ex:projectState a rdfs:Property ;
        rdfs:range tags:Tag ;
        // rdfs:range tags:Tag { open|closed }
        .

    ex:propertyState a rdfs:Property ;
        rdfs:range tags:Tag ;
        //  ex:propertyState [interested|acquiring|renting|leasing|renting_out|leasing_out|own]
        .


::

    User
    - name
    - email
    - profilePhoto
    - bannerPhoto

    Group
    - name
    - desc
    - image
    - profilePhoto
    - bannerPhoto

    Project
    * primaryGroup
    - name
    - desc
    - image
    - profilePhoto
    - bannerPhoto
    * tags[]
    * messages[]
    * todos[]

    PropertyProject(Project)
    * property
    * things[]

    Property
    - name
    - desc
    - image
    - profilePhoto
    - bannerPhoto
    = maintenance history
    = inventory
      = food
      = things
    = utilities
      = numbers, websites
      = bills

::


    user           /{userid}[/]                           -- /westurner
        a ex:User
        ex:id
        schema:name
        schema:desc
        schema:image
        ex:bannerImage
        ex:thumbnailImage

    group           /{groupid}[/]                         -- /g2
        a ex:Group
        ex:id
        schema:name
        schema:desc
        schema:image
        ex:bannerImage
        ex:thumbnailImage


        project     /{groupid}/{projectid}[/]             -- /g2/zxy214 || /g2/project-two
        property    /{groupid}/{propertyid}[/]            -- /g2/zxy214 || /g2/studio-two
            a ex:Property
            ex:id
            schema:name
            schema:desc
            schema:image

            things  /{groupid}/{propertyid}/{thingid}[/]  -- /g2/studio-two/dcb765
                a schema:Thing
                ex:id
                schema:name
                schema:desc
                schema:image

                messages: [ ex:Message ]
                todos: [ ex:Todo ]
                events: [ schema:Event ]

                thing > {rdf:type}
                    a 
                    schema:name
                    schema:desc *
                    schema:image
                    tags:tag

                    thing > todo
                        a ex:ProductTodo

    tags            /tag/{tagid}                          -- /tag/in_progress
        a tags:Tag;

        """
        SELECT ?s ?tag ?lastModified 
        WHERE {
            ?s tags:tag ?tag .
            ?s ex:lastModified ?lastModified .
        }
        ORDER BY ?tag, ?lastModified
        """

        from surf.query import select, describe, ask
        from surf.query.translator.sparql import SparqlTranslator 
        from surf.rdf import URIRef

        query = select(
            ("?s", "?tag", "?lastModified"),
        ).where(
            ("?s", TAGS.tag, "?tag"),
            ("?s", EX.lastModified, "?lastModified"),
        ).order_by(
            ("?tag", "?lastModified")
        )

        sparql_query = SparqlTranslator(query).translate()

        for subj, tag, lastModified;
            for result in group:
                obj = session.get_resource(subj, subj.type[] )



- [ ] group.crud
- [ ] group.create(request.user.id, request.user.label*)
- [ ] group.add_property
- [ ] property.crud

  - [ ] GROUP_PROPERTY_URLS.append((group, name), (property.id))
  - [ ] property.add_thing
  - [ ] property.thing.update(date, {data})


Views
*******

- [ ] stream

::
                                                            -- /
    {%- datestr=(date-yyyy) %}
    <h2><a href="#{{datestr}}" id="{{datestr}}">{{datestr}}</a></h2>
    {%- datestr=(date-yyyy-mm) %}
    <h3><a href="#{{datestr}}" id="{{datestr}}">{{datestr}}</a></h3>
    {%- datestr=(date-yyyy-mm-dd) %}
    <h4><a href="#{{datestr}}" id="{{datestr}}">{{datestr}}</a></h4>
    {% for thing in daily %}

       <li class="row thing" about="{{ thing.url }}" typeof="{{thing.types}}">
        <a href="{{thing.url}}">{{date.isoformat()}}</a>
        {#- [icons_for_types(list(thing[RDF.type]))] #}
        {%- for type in thing.objects(RDF.type) %}
        <a href="/things/{{type}}"
            class="smallicon-{{type}}"
            title="{{type.label }}"></a>
        {% endfor %}
        <span class="thing_name" property="schema:name">{{name}}</span>
        <span class="thing_description" property="schema:description"
        >{{description | more}}</span>
       </li>

    {% endfor %}
