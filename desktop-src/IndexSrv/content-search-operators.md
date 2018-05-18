---
title: Content Search Operators
description: Content Search Operators
ms.assetid: 'aea33c6e-f299-4963-85ae-473963cddfbc'
---

# Content Search Operators

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following operators describe search operations on columns containing text. These operators generally behave like any other Boolean operators. When used in conjunction with the DBOP\_content\_select operator, however, the resulting tables include two special columns describing the hit count and rank.

<dl> <dt>

<span id="DBOP_content_select"></span><span id="dbop_content_select"></span><span id="DBOP_CONTENT_SELECT"></span>DBOP\_content\_select
</dt> <dd>

This operator is similar to the DBOP\_select operator. It takes a table T and Boolean expression (selection condition) as input, and produces a table R as output. The rows in R are those rows that satisfy the selection condition. However, the columns of R include all the columns of T plus three additional columns representing the hit count, a rank, and a rank vector (which together represent the quality of the match).

</dd> <dt>

<span id="DBOP_content__DBOP_content_freetext"></span><span id="dbop_content__dbop_content_freetext"></span><span id="DBOP_CONTENT__DBOP_CONTENT_FREETEXT"></span>DBOP\_content, DBOP\_content\_freetext
</dt> <dd>

These operators are used to express content searches for words or phrases found in a column. They take one required input: a column name specifying the column in which to search. They have two special column identifiers. The first, PROPID\_STG\_CONTENTS, means "look in the object contents" for data providers that have rows that actually are objects. The second, PROPID\_ QUERY\_ALL, means "look in all columns."

The text search pattern is stored in the [**DBCONTENT**](dbcontent.md) structure within the node. DBOP\_content\_freetext differs from DBOP\_content in that it instructs the query engine to use all of its text-processing tricks in evaluating the restriction. The DBOP\_content node may specify a method to generate words matching a pattern (this field is ignored for DBOP\_content\_freetext), which determines the manner in which the initial query term is expanded before searching text. GENERATE\_METHOD\_EXACT matches only the word or phrase specified in the content node. GENERATE\_METHOD\_PREFIX matches all words that begin with the text specified in the node. GENERATE\_METHOD\_INFLECT causes linguistic inflection of the specified word. The English word "run", for example, may expand to "run", "running", "ran", "runs", and so forth. Providers may support other generation methods (for example, GENERATE\_METHOD\_MISSPELLING or GENERATE\_METHOD\_REGEX). The generation methods specified in this node are mutually exclusive. Not all of the levels specified above are available for each language. If GENERATE\_METHOD\_PREFIX or GENERATE\_METHOD\_INFLECT is used with a phrase (multiple words), the expansion applies to each word separately. The exact method of splitting a phrase into words is implementation-specific. These nodes also have a weight field, which may be used by a sophisticated data consumer to give more or less weight in hit-ranking to matches on this particular content restriction. The output of these operators is Boolean. The arguments internal to this node are specified using the **DBCONTENT** structure.

PSGUID\_QUERY is the GUID for the property set for special content columns. The following are some of the interesting columns in this set:


```
#define PROPID_QUERY_RANKVECTOR (0x2) // column used to return rank
                                      // values of the
                                      // content_vector_or operator
 
#define PROPID_QUERY_RANK (0x3) // column used to return the final
                                // rank of each row
 
#define PROPID_QUERY_HITCOUNT (0x4) // column used to return the
                                    // number of content hits found
                                    // in a row
 
#define PROPID_QUERY_ALL    (0x6) // search in all text associated
                                  // with a row
 
#define PROPID_STG_CONTENTS (0x13) // search inside the contents on
                                   // an object
```



</dd> <dt>

<span id="DBOP_content_proximity"></span><span id="dbop_content_proximity"></span><span id="DBOP_CONTENT_PROXIMITY"></span>DBOP\_content\_proximity
</dt> <dd>

Proximity nodes are used to rank hits within queries that search for several different pieces of text. The rank of an object matched by a proximity node increases as the words and phrases move closer together. The formula used to compute rank is specific to a given implementation. Generally a proximity node should be used as an n-ary **AND** node among multiple content restrictions. The internal arguments of this node are a proximity unit (**DWORD**), a proximity distance (**ULONG**), and a weight on the node (**LONG**), all specified with the [**DBCONTENTPROXIMITY**](dbcontentproximity.md) structure.

The proximity units specified by the [proximity unit constants](proximity-unit-constants.md) are supported.

The node takes two or more input subtrees, each of which should contain DBOP\_content, DBOP\_content\_freetext, DBOP\_content\_proximity, DBOP\_and, DBOP\_or, or DBOP\_not nodes. The output of the node is Boolean. It is logically similar to a bitwise **AND** operator in that all input subtrees must evaluate to TRUE to produce a true value.

</dd> <dt>

<span id="DBOP_content_scope"></span><span id="dbop_content_scope"></span><span id="DBOP_CONTENT_SCOPE"></span>DBOP\_content\_scope
</dt> <dd>

\[ TBD \]

</dd> <dt>

<span id="DBOP_content_table"></span><span id="dbop_content_table"></span><span id="DBOP_CONTENT_TABLE"></span>DBOP\_content\_table
</dt> <dd>

\[ TBD \]

</dd> <dt>

<span id="DBOP_content_vector_or"></span><span id="dbop_content_vector_or"></span><span id="DBOP_CONTENT_VECTOR_OR"></span>DBOP\_content\_vector\_or
</dt> <dd>

Used to support advanced content-retrieval models. This node acts as an n-ary **OR** node, with two main differences. First, when a vector node is used the programmer has the option of retrieving a rank vector for each object, as a special, well-known column. This vector contains the rank of each child node in the vector. Second, the formula used to compute the overall rank of the vector may be specified. The ranking methods specified by the [vector rank constants](vector-rank-constants.md) are supported.

There may be at most one vector node in the tree. The internal arguments of this node are a ranking method (**DWORD**) and a weight on the node (**LONG**), specified within the [**DBCONTENTVECTOR**](dbcontentvector.md) structure.

There are two or more children, of exactly the same type as DBOP\_content\_proximity above. This operator produces Boolean output. It acts as an n-ary**OR** operation of the input subtrees.

</dd> </dl>

 

 




