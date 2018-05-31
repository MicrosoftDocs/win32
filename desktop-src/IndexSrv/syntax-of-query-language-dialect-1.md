---
title: Syntax of Query Language Dialect 1
description: Syntax of Query Language Dialect 1
ms.assetid: b204520a-d6ff-4436-bb9a-0989114f973c
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Syntax of Query Language Dialect 1

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following EBNF production rules define the syntax of the original Indexing Service query language, Query Dialect 1. Terminal symbols are case insensitive: **or**, **OR**, **Or**, and **oR** are equivalent. The production rules give terminal symbols in lowercase only. A query containing a comma denotes a vector space query. Weight is specified using the **\[** Digits **\]** construct, where the value can be 0 to 1000.

<dl> <dt>

<span id="Query_____________________________________________start_symbol___"></span><span id="query_____________________________________________start_symbol___"></span><span id="QUERY_____________________________________________START_SYMBOL___"></span>Query =                                        (\* start symbol \*)
</dt> <dd>

QExpression \[ **,** Query \] ;

</dd> <dt>

<span id="QExpression__"></span><span id="qexpression__"></span><span id="QEXPRESSION__"></span>QExpression =
</dt> <dd>

QTerm \[ ( **or** { · }- \| **\|** ) QExpression \] ;

</dd> <dt>

<span id="QTerm__"></span><span id="qterm__"></span><span id="QTERM__"></span>QTerm =
</dt> <dd>

\[ **not** { · }- \| **!** \] QProperty \[ **\[** Digits **\]** \] \[ ( **and** { · }- \| **&** ) QTerm \] ;

</dd> <dt>

<span id="QProperty__"></span><span id="qproperty__"></span><span id="QPROPERTY__"></span>QProperty =
</dt> <dd>

( \[ **@** Property \] QFactor )

\| ( **\#** Property \[ **=** \] Regex )

\| ( **$** Property QPhrase ) ;

</dd> <dt>

<span id="QFactor__"></span><span id="qfactor__"></span><span id="QFACTOR__"></span>QFactor =
</dt> <dd>

QGroup

\| ( **(** Query **)** )

\| ( Operator \[ **^a** \| **^s** \] Phrase ) ;        (\* **^a**\|**^s** only for vector properties \*)

</dd> <dt>

<span id="QGroup__"></span><span id="qgroup__"></span><span id="QGROUP__"></span>QGroup =
</dt> <dd>

QPhrase \[ ( **near** { · }- \| **~** ) QGroup \] ;

</dd> <dt>

<span id="QPhrase__"></span><span id="qphrase__"></span><span id="QPHRASE__"></span>QPhrase =
</dt> <dd>

( Phrase \[ **\*** \| **\*\*** \] )

\| Regex

\| ( **"** AnyExceptQuote **"** \[ **\*** \| **\*\*** \] ) ;

</dd> <dt>

<span id="Property__"></span><span id="property__"></span><span id="PROPERTY__"></span>Property =
</dt> <dd>

Phrase

\| ( **{** \[ { Phrase **,** } Phrase \] **}** ) ;

</dd> <dt>

<span id="Phrase___"></span><span id="phrase___"></span><span id="PHRASE___"></span>Phrase = 
</dt> <dd>

Any                                            (\* string phrase \*)

\| ( \[ **-** \] Digits )                            (\* integer phrase \*)

\| ( \[ **-** \] Digits \[ **.** Digits \] )            (\* float phrase \*)

\| ( **t** \| **true** \| **false** \| Any )            (\* Bool phrase; Any = **false** \*)

\| DatePhrase                                (\* date and time phrase \*)

\| ( Digits **.** Digits )                         (\* currency phrase: dollars.cents \*)

\| GUIDPhrase ;                            (\* globally unique identifier phrase \*)

</dd> <dt>


</dt> <dd>

(\* The following rule only prepares for the query engine, which does \*)

(\* the final parsing. See [Pattern-Matching Queries](pattern-matching-queries.md) for the full syntax. \*)

</dd> <dt>

<span id="Regex__"></span><span id="regex__"></span><span id="REGEX__"></span>Regex =
</dt> <dd>

**"** AnyExceptQuote **"**

\| ( ? Any character sequence preceding · ?)

\| ( ? Any character sequence preceding **)** not preceded by **!** ? ) ;

</dd> <dt>

<span id="DatePhrase_____________________________________yyyy_mm_dd_hh_mm_ss_msec___"></span><span id="datephrase_____________________________________yyyy_mm_dd_hh_mm_ss_msec___"></span><span id="DATEPHRASE_____________________________________YYYY_MM_DD_HH_MM_SS_MSEC___"></span>DatePhrase =                                (\* yyyy/mm/dd hh:mm:ss:msec \*)
</dt> <dd>

( **-** { Digits ( **h** \| **n** \| **s** \| **y** \| **m** \| **d** \| **w** ) }- )

\| ( Digits ( **/** ) Digits ( **/** ) Digits \[ · Digits **:** Digits **:** Digits \[ **:** Digits \] \] )

\| ( Digits **-** Digits **-** Digits \[ · Digits **:** Digits **:** Digits \[ **:** Digits \] \] ) ;

</dd> <dt>

<span id="GUIDPhrase__"></span><span id="guidphrase__"></span><span id="GUIDPHRASE__"></span>GUIDPhrase =
</dt> <dd>

**{** **0x** 8 \* HexDigit **,** 2 \* ( **0x** 4 \* HexDigit **,** )

**{** **0x** 2 \* HexDigit 7 \* ( **,** **0x** 2 \* HexDigit ) **}** ;

</dd> <dt>

<span id="Operator__"></span><span id="operator__"></span><span id="OPERATOR__"></span>Operator =
</dt> <dd>

**=** \| **!=** \| **&gt;** \| **&gt;=** \| **&lt;** \| **&lt;=** \| **^a** \| **^s** ;

</dd> <dt>

<span id="Digits__"></span><span id="digits__"></span><span id="DIGITS__"></span>Digits =
</dt> <dd>

{ DecimalDigit }- ;

</dd> <dt>

<span id="DecimalDigit__"></span><span id="decimaldigit__"></span><span id="DECIMALDIGIT__"></span>DecimalDigit =
</dt> <dd>

**0** \| **1** \| **2** \| **3** \| **4** \| **5** \| **6** \| **7** \| **8** \| **9** ;

</dd> <dt>

<span id="HexDigit__"></span><span id="hexdigit__"></span><span id="HEXDIGIT__"></span>HexDigit =
</dt> <dd>

DecimalDigit \| **a** \| **b** \| **c** \| **d** \| **e** \| **f** ;

</dd> <dt>

<span id="Any__"></span><span id="any__"></span><span id="ANY__"></span>Any =
</dt> <dd>

? Any character sequence ? - Excluded ;

</dd> <dt>

<span id="Excluded__"></span><span id="excluded__"></span><span id="EXCLUDED__"></span>Excluded =
</dt> <dd>

**{** \| **}** \| **!** \| **&** \| **\|** \| **~** \| **\*** \| **@** \| **\#** \| **(** \| **)** \| **\[** \| **\]** \| **,** \| **=** \| **&lt;** \| **&gt;** \| **\\n** \| **"** \| **^** \| **$** ;

</dd> <dt>

<span id="AnyExceptQuote__"></span><span id="anyexceptquote__"></span><span id="ANYEXCEPTQUOTE__"></span>AnyExceptQuote =
</dt> <dd>

? Any character sequence ? - **"** ;        (\* quoted **"** ( = **""** ) is OK \*)

</dd> </dl>

 

 




