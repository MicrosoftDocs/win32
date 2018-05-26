---
title: Syntax of Query Language Dialect 2
description: Syntax of Query Language Dialect 2
ms.assetid: d1e412b5-2dd0-4690-b6cf-78660a581ab2
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Syntax of Query Language Dialect 2

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following EBNF production rules define the syntax of the extensible Indexing Service query language, Query Dialect 2. Terminal symbols are case insensitive: **or**, **OR**, **Or**, and **oR** are equivalent. The production rules give terminal symbols in lowercase only.

<dl> <dt>

<span id="Query_____________________________________________________start_symbol___"></span><span id="query_____________________________________________________start_symbol___"></span><span id="QUERY_____________________________________________________START_SYMBOL___"></span>Query =                                                (\* start symbol \*)
</dt> <dd>

( \[ Query ( **or** { · }- \| **\|** )\] AndTerm )

\| ( **not** { · }- \| **!** ) Query ;

</dd> <dt>

<span id="AndTerm__"></span><span id="andterm__"></span><span id="ANDTERM__"></span>AndTerm =
</dt> <dd>

NearTerm

\| ( ( **not** { · }- \| **!** ) PropTerm )

\| ( AndTerm ( **and** { · }- \| **&** ) \[ ( **not** { · }- \| **!** ) \] NearTerm ) ;

</dd> <dt>

<span id="NearTerm__"></span><span id="nearterm__"></span><span id="NEARTERM__"></span>NearTerm =
</dt> <dd>

CoerceTerm

\| ( NearTerm ( **{near** { · }- \| **~** ) CoerceTerm )

\| ( NearTerm NearElement **}** CoerceTerm ) ;

</dd> <dt>

<span id="PropTerm__"></span><span id="propterm__"></span><span id="PROPTERM__"></span>PropTerm =
</dt> <dd>

( Property \[ **=** \] Regex \[ **{/prop}** \] )

\| ( Property Operator Value \[ **{/prop}** \] ) ;

</dd> <dt>

<span id="CoerceTerm__"></span><span id="coerceterm__"></span><span id="COERCETERM__"></span>CoerceTerm =
</dt> <dd>

( \[ Generate \] NestTerm \[ **{/generate}** \] )

**‹**\| ( \[ Generate \] **{/coerce}** \[ Generate \] NestTerm \[ **{/generate}** \] )

**›**\| ( \[ Generate \] Weight \[ Generate \] NestTerm \[ **{/generate}** \] ) ;

</dd> <dt>

<span id="NearElement__"></span><span id="nearelement__"></span><span id="NEARELEMENT__"></span>NearElement =
</dt> <dd>

White

\| **,**

\| ( **dist** { · } **=** { · } Digits )

\| ( **unit** { · } **=** { · } **‹**( **›word** **‹**\| **sent** \| **par** \| **chap** ) **›**) ;

</dd> <dt>

<span id="Property__"></span><span id="property__"></span><span id="PROPERTY__"></span>Property =
</dt> <dd>

\[ LongPropName \| ShortPropName \] ;

</dd> <dt>


</dt> <dd>

(\* The following rule only prepares for the query engine, which does \*)

(\* the final parsing. See [Pattern-Matching Queries](pattern-matching-queries.md) for the full syntax. \*)

</dd> <dt>

<span id="Regex__"></span><span id="regex__"></span><span id="REGEX__"></span>Regex =
</dt> <dd>

( **{regex}** **"** \[ AnyExceptQuote \] **"** **{/regex}** )

\| ( **{regex}** \[ AnyExceptCurlyOpen \] **{/regex}** )

\| ( **{regex}** \[ \[ AnyExceptNewline \] **\|** \[ AnyExceptNewline \] \] **{/regex}** ) ;

</dd> <dt>

<span id="Operator__"></span><span id="operator__"></span><span id="OPERATOR__"></span>Operator =
</dt> <dd>

**=** \| **!=** \| **&gt;** \| **&gt;=** \| **&lt;** \| **&lt;=** \| **^a** \| **^s**

\| ( **=** { · }**^s** \| **^s** { · } **=** )

\| ( **!=** { · } **^s** \| **^s** { · } **!=** )

\| ( **&gt;** { · } **^s** \| **^s** { · } **&gt;** )

\| ( **&gt;=** { · } **^s** \| **^s** { · } **&gt;=** )

\| ( **&lt;** { · } **^s** \| **^s** { · } **&lt;** )

\| ( **&lt;=** { · } **^s** \| **^s** { · } **&lt;=** )

\| ( **^s** { · } **^a** )

\| ( **^s** { · } **^s** )

\| ( **^a** { · } **=** )

\| ( **^a** { · } **!=** )

\| ( **^a** { · } **&gt;** )

\| ( **^a** { · } **&gt;=** )

\| ( **^a** { · } **&lt;** )

\| ( **^a** { · } **&lt;=** )

\| ( **^a** { · } **^a** )

\| ( **^a** { · } **^s** ) ;

</dd> <dt>

<span id="Value__"></span><span id="value__"></span><span id="VALUE__"></span>Value =
</dt> <dd>

Phrase

\| Freetext

\| VectorValue ;

</dd> <dt>

<span id="Generate__"></span><span id="generate__"></span><span id="GENERATE__"></span>Generate =
</dt> <dd>

( **{generate** { · }- **method** { · } **=** { · } **prefix** { · } **}** )

\| ( **{generate** { · }- **method** { · } **=** { · } **inflect** { · } **}** ) ;

</dd> <dt>

<span id="NestTerm__"></span><span id="nestterm__"></span><span id="NESTTERM__"></span>NestTerm =
</dt> <dd>

VectorTerm

\| Term

\| ( **(** Query **)** ) ;

</dd> <dt>

<span id="Weight__"></span><span id="weight__"></span><span id="WEIGHT__"></span>Weight =
</dt> <dd>

**{weight** { · }- **value** { · } **=** { · } ( **0** \| **1** \| ( **0.** { DecimalDigit } ) \| ( **1.** { **0** } ) \| ( **.** { DecimalDigit }- ) ) ;

</dd> <dt>

<span id="LongPropName__"></span><span id="longpropname__"></span><span id="LONGPROPNAME__"></span>LongPropName =
</dt> <dd>

( **{prop** { · }- **name** { · } **=** { · } **"** \[ AnyExceptQuote \] **"** { · } **}** )

\| ( **{prop** { · }- **name** { · } **=** { · } AnyExceptQuoteCurlyCloseSpace \[ AnyExceptCurlyClose \] **}** ) ;

</dd> <dt>

<span id="ShortPropName__"></span><span id="shortpropname__"></span><span id="SHORTPROPNAME__"></span>ShortPropName =
</dt> <dd>

( ( **@** \| **$** \| **\#** ) **"** AnyExceptQuote **"** )

\| ( ( **@** \| **$** \| **\#** ) AnyExceptExcluded ) ;

</dd> <dt>

<span id="Phrase__"></span><span id="phrase__"></span><span id="PHRASE__"></span>Phrase =
</dt> <dd>

( LongPhrase \| ShortPhrase ) \[ **\*** \| **\*\*** \] ;

</dd> <dt>

<span id="Freetext__"></span><span id="freetext__"></span><span id="FREETEXT__"></span>Freetext =
</dt> <dd>

( LongFreetext \| ShortFreetext ) \[ **\*** \| **\*\*** \] ;

</dd> <dt>

<span id="VectorValue__"></span><span id="vectorvalue__"></span><span id="VECTORVALUE__"></span>VectorValue =
</dt> <dd>

EmptyVector

\| SingletVector

\| MultiVector **)** ;

</dd> <dt>

<span id="LongPhrase__"></span><span id="longphrase__"></span><span id="LONGPHRASE__"></span>LongPhrase =
</dt> <dd>

( **{phrase}** { · } **"** \[ AnyExceptQuote \] **"** { · } **{/phrase}** )

\| ( **{phrase}** \[ AnyExceptCurlyOpen \] **{/phrase}** ) ;

</dd> <dt>

<span id="ShortPhrase__"></span><span id="shortphrase__"></span><span id="SHORTPHRASE__"></span>ShortPhrase =
</dt> <dd>

( **"** \[ AnyExceptQuote \] **"** )

\| ( AnyExceptMany \[ AnyExceptOp \] \[ · \] ) ;

</dd> <dt>

<span id="LongFreetext__"></span><span id="longfreetext__"></span><span id="LONGFREETEXT__"></span>LongFreetext =
</dt> <dd>

( **{freetext}** { · } **"** \[ AnyExceptQuote \] **"** { · } **{/freetext}** )

\| ( **{freetext}** \[ AnyExceptCurlyOpen \] **{/freetext}** ) ;

</dd> <dt>

<span id="ShortFreetext__"></span><span id="shortfreetext__"></span><span id="SHORTFREETEXT__"></span>ShortFreetext =
</dt> <dd>

AnyExceptMany \[ AnyExceptOp \] \[ · \] ;

</dd> <dt>

<span id="VectorTerm__"></span><span id="vectorterm__"></span><span id="VECTORTERM__"></span>VectorTerm =
</dt> <dd>

VectorSpec **{/vector}** ;

</dd> <dt>

<span id="Term__"></span><span id="term__"></span><span id="TERM__"></span>Term =
</dt> <dd>

PropTerm

\| ( Property \[ **contains** { · }- \] Phrase \[ **{/prop}** \] )

\| ( Property \[ **contains** { · }- \] Generate Phrase \[ **{/generate}** \] \[ **{/prop}** ) \]

\| ( Property \[ **contains** { · }- \] Query )

\| ( Property \[ **contains** { · }- \] Freetext \[ **{/prop}** \] ) ;

</dd> <dt>

<span id="EmptyVector__"></span><span id="emptyvector__"></span><span id="EMPTYVECTOR__"></span>EmptyVector =
</dt> <dd>

**(** **)** ;

</dd> <dt>

<span id="SingletVector__"></span><span id="singletvector__"></span><span id="SINGLETVECTOR__"></span>SingletVector =
</dt> <dd>

( **(** Phrase **)** )

\| ( **(** Freetext **)** ) ;

</dd> <dt>

<span id="MultiVector__"></span><span id="multivector__"></span><span id="MULTIVECTOR__"></span>MultiVector =
</dt> <dd>

( VectorElement VectorElement )

\| ( MultiVector VectorElement ) ;

</dd> <dt>

<span id="VectorSpec__"></span><span id="vectorspec__"></span><span id="VECTORSPEC__"></span>VectorSpec =
</dt> <dd>

( VectorMethod **{ve}** Query )

\| ( VectorSpec **{ve}** Query ) ;

</dd> <dt>

<span id="VectorElement__"></span><span id="vectorelement__"></span><span id="VECTORELEMENT__"></span>VectorElement =
</dt> <dd>

White

\| **;**

\| ( **"** \[ AnyExceptQuote \] **"** )

\| ( AnyExceptVector \[ AnyExceptSemiClose \] ( **;** \| **)** ) ) ;

</dd> <dt>

<span id="VectorMethod__"></span><span id="vectormethod__"></span><span id="VECTORMETHOD__"></span>VectorMethod =
</dt> <dd>

( **{vector** { · }- **rankmethod** { · } **=** { · } **"** \[ AnyExceptQuote \] **"** { · } **}** )

\| ( **{vector** { · }- **rankmethod** { · } **=** \[ AnyExceptCurlyClose \] **}** ) ;

</dd> <dt>

<span id="Digits__"></span><span id="digits__"></span><span id="DIGITS__"></span>Digits =
</dt> <dd>

{ DecimalDigit }- ;

</dd> <dt>

<span id="DecimalDigit__"></span><span id="decimaldigit__"></span><span id="DECIMALDIGIT__"></span>DecimalDigit =
</dt> <dd>

**0** \| **1** \| **2** \| **3** \| **4** \| **5** \| **6** \| **7** \| **8** \| **9** ;

</dd> <dt>

<span id="White__"></span><span id="white__"></span><span id="WHITE__"></span>White =
</dt> <dd>

· \| **\\t** \| **\\n** \| **\\f** \| **\\r** ;

</dd> <dt>

<span id="AnyExceptQuote__"></span><span id="anyexceptquote__"></span><span id="ANYEXCEPTQUOTE__"></span>AnyExceptQuote =
</dt> <dd>

? Any character sequence ? - **"** ;        (\* quoted **"** ( = **""** ) is OK \*)

</dd> <dt>

<span id="AnyExceptNewline__"></span><span id="anyexceptnewline__"></span><span id="ANYEXCEPTNEWLINE__"></span>AnyExceptNewline =
</dt> <dd>

? Any character sequence ? - **\\n** ;

</dd> <dt>

<span id="AnyExceptCurlyOpen__"></span><span id="anyexceptcurlyopen__"></span><span id="ANYEXCEPTCURLYOPEN__"></span>AnyExceptCurlyOpen =
</dt> <dd>

? Any character sequence ? - **{** ;

</dd> <dt>

<span id="AnyExceptCurlyClose__"></span><span id="anyexceptcurlyclose__"></span><span id="ANYEXCEPTCURLYCLOSE__"></span>AnyExceptCurlyClose =
</dt> <dd>

? Any character sequence ? - **}** ;

</dd> <dt>

<span id="AnyExceptSemiClose__"></span><span id="anyexceptsemiclose__"></span><span id="ANYEXCEPTSEMICLOSE__"></span>AnyExceptSemiClose =
</dt> <dd>

? Any character sequence ? - ( **;** \| **)** ) ;

</dd> <dt>

<span id="AnyExceptQuoteCurlyCloseSpace__"></span><span id="anyexceptquotecurlyclosespace__"></span><span id="ANYEXCEPTQUOTECURLYCLOSESPACE__"></span>AnyExceptQuoteCurlyCloseSpace =
</dt> <dd>

? Any character sequence ? - ( **"** \| **}** \| · ) ;

</dd> <dt>

<span id="AnyExceptVector__"></span><span id="anyexceptvector__"></span><span id="ANYEXCEPTVECTOR__"></span>AnyExceptVector =
</dt> <dd>

? Any character sequence ? - ( **"** \| **;** \| · ) ;

</dd> <dt>

<span id="AnyExceptOp__"></span><span id="anyexceptop__"></span><span id="ANYEXCEPTOP__"></span>AnyExceptOp =
</dt> <dd>

? Any character sequence ? - ( **&** \| **~** \| **\|** \| **{** \| **)** \| · ) ;

</dd> <dt>

<span id="AnyExceptExcluded__"></span><span id="anyexceptexcluded__"></span><span id="ANYEXCEPTEXCLUDED__"></span>AnyExceptExcluded =
</dt> <dd>

? Any character sequence ? - ( **"** \| · \| **&lt;** \| **&gt;** \| **=** \| **!** \| **&** \| **\|** \| **~** \| **^** ) ;

</dd> <dt>

<span id="AnyExceptMany__"></span><span id="anyexceptmany__"></span><span id="ANYEXCEPTMANY__"></span>AnyExceptMany =
</dt> <dd>

? Any character sequence ? - ( **\#** \| **$** \| **@** \| **~** \| **&** \| **\|** \| **&lt;** \| **&gt;** \| **=** \| **!** \| **^**\| **\*** \| **"** \| **(** \| **)** \| **{** \| · ) ;

</dd> </dl>

 

 




