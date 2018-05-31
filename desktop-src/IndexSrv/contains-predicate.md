---
title: CONTAINS Predicate
description: CONTAINS Predicate
ms.assetid: b7416c8f-3270-466a-89ac-32f7e30ccd48
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CONTAINS Predicate

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **CONTAINS** predicate provides several text-matching options for building queries. Typically, you use this predicate to query the Contents property, the text contents of a file. You can also query other textual properties with content, such as DocTitle, DocSubject, or a user-defined property. This predicate is an optional part of the optional **WHERE** clause of the **SELECT** statement.

``` syntax
SELECT Select_List | *
       FROM_Clause
       [WHERE CONTAINS ([Column_Reference, ] 'Content_Search_Conditions')
       [ORDER_BY_Clause]
```

### Parameters

<dl> <dt>

<span id="Select_List"></span><span id="select_list"></span><span id="SELECT_LIST"></span>*Select\_List*
</dt> <dd>

Specifies the list of column aliases (properties) making up the table (rowset) that is returned as a result of the query.

</dd> <dt>

<span id="___asterisk_"></span><span id="___ASTERISK_"></span>*\** (asterisk)
</dt> <dd>

Specifies all columns. This option is valid only when the *FROM\_Clause* parameter references a predefined view or a temporary view.

</dd> <dt>

<span id="FROM_Clause"></span><span id="from_clause"></span><span id="FROM_CLAUSE"></span>*FROM\_Clause*
</dt> <dd>

Specifies the files on which to perform the search. For details about this parameter, see [FROM Clause](from-clause.md).

</dd> <dt>

<span id="Column_Reference"></span><span id="column_reference"></span><span id="COLUMN_REFERENCE"></span>*Column\_Reference*
</dt> <dd>

Specifies the column alias. If you do not specify a column reference, the default is the Contents property. For example, the following two clauses are equivalent:


```
... WHERE CONTAINS (Contents, 'European')
... WHERE CONTAINS ('European')
```



</dd> <dt>

<span id="Content_Search_Conditions"></span><span id="content_search_conditions"></span><span id="CONTENT_SEARCH_CONDITIONS"></span>*Content\_Search\_Conditions*
</dt> <dd>

Specifies one or more search terms. When using more than one search term, connect the terms with **AND**, **AND NOT** or **OR** operators. When specifying Boolean operators, both the text ( **AND** , **OR** , **NOT** ) and symbolic (**&**, **\|**, **!** ) forms are acceptable.

> [!Note]  
> Always place spaces around the text Boolean operators.

 

When the content search condition consists of statements enclosed in parentheses, expressions in parentheses are evaluated first. After the parenthetical expressions are evaluated, the following rules apply:

-   **NOT** is evaluated before **AND**.
-   **NOT** can only occur after **AND** (as in **AND NOT**; the combination **OR NOT** is not allowed).
-   **AND** is evaluated before **OR**.
-   **AND** expressions are associative and can be applied in any order. For example, A **AND** B **AND** C, is the same as (A **AND** B) **AND** C, which is the same as A **AND** (B **AND** C).
-   **OR** expressions are associative and can be applied in any order.

> [!Note]  
> It is illegal to place a **NOT** operator before content query predicates (**CONTAINS** and **FREETEXT**) unless the **NOT** operator is preceded by an **AND** operator.

 

</dd> <dt>

<span id="ORDER_BY_Clause"></span><span id="order_by_clause"></span><span id="ORDER_BY_CLAUSE"></span>*ORDER\_BY\_Clause*
</dt> <dd>

Specifies the ordering of the resulting rowset. This clause is optional. For details about this parameter, see [ORDER BY Clause](order-by-clause.md).

</dd> </dl>

### Remarks

Index Server 1.*x* and 2.0 required a &gt; 0 comparison operation at the end of the **CONTAINS** predicate; for example, **CONTAINS( ... ) &gt;0**. Beginning with Indexing Service 3.0, the comparison operation is neither required nor recommended, but is supported for compatibility with earlier versions.

The **CONTAINS** predicate uses string literals, so certain conventions must be followed when using single and double quotes. In addition there are several types of quoted material, which produce different types of matches.

## Quotes in Basic String Literals

The **CONTAINS** predicate uses the following conventions when dealing with single and double quotes in basic string literals.

-   If a basic string literal contains spaces, always use double quotes as delimiters. For example:
    ```
    '"Phrase With Spaces"'
    ```

    

-   If a basic string literal with no spaces contains a single quote, use two single quotes to specify the single-quote character. For example:
    ```
    'Phrase'Without'Spaces'
    ```

    

-   If a basic string literal with spaces contains a single quote, use double quotes as delimiters. For example:
    ```
    '"Phrase 'With' Spaces"'
    ```

    

-   If a basic string literal with no spaces contains a double quote, two double quotes are not necessary. For example:
    ```
    'Phrase"Without"Spaces'
    ```

    

-   If a basic string literal with spaces contains a double quote, use two double quotes to specify the double-quote character. For example:
    ```
    '"Phrase ""With"" Spaces"'
    ```

    

## Types of CONTAINS Matches

The following table lists the types of matches along with descriptions of how they work.



| Match Type                                                  | Description                                                                 |
|-------------------------------------------------------------|-----------------------------------------------------------------------------|
| [Simple Match](#simple-match)                               | Matches the specified word or phrase.                                       |
| [Word Prefix Match](#word-prefix-match)                     | Uses the wildcard character "\*" to match words containing the same prefix. |
| [Proximity Match](#proximity-match)                         | Searches for words that are close to one another.                           |
| [Linguistic Generation Match](#linguistic-generation-match) | Matches various tenses of verbs, plural, or singular of nouns.              |
| [Weighted Match](#weighted-match)                           | Returns rows that match a weighted list of words.                           |



 

### Simple Match

In a simple match, the word or phrase must be an exact match; however, the matching is not case sensitive. Multiple consecutive words are treated as a single phrase, and must appear in exactly the same order in the matching document. If a phrase contains blank spaces between words or punctuation marks, it must be enclosed in double quotes.

``` syntax
<b>CONTAINS</b> <b>(</b>[<i>Column_Reference</i>,]
          '<b>"</b><i>Word_or_Phrase</i><b>"</b>
          [ <i>Boolean_Operator</i> <b>"</b><i>Word_or_Phrase</i><b>"</b>]
           ... '<b>)</b>
```

### Parameters

<dl> <dt>

<span id="Column_Reference"></span><span id="column_reference"></span><span id="COLUMN_REFERENCE"></span>*Column\_Reference*
</dt> <dd>

Specifies the column name (alias). Its data type must be compatible with the format of the *Word\_or\_Phrase* parameter specified.

</dd> <dt>

<span id="Word_or_Phrase"></span><span id="word_or_phrase"></span><span id="WORD_OR_PHRASE"></span>*Word\_or\_Phrase*
</dt> <dd>

Specifies the literal of type Basic String to match.

</dd> <dt>

<span id="Boolean_Operator"></span><span id="boolean_operator"></span><span id="BOOLEAN_OPERATOR"></span>*Boolean\_Operator*
</dt> <dd>

Specifies the Boolean operator to use, following the precedence rules previously stated, that combines the comparison predicates.

</dd> </dl>

### Examples

The following example searches the DocAuthor property of all files from the default scope, and retrieves rows consisting of the DocTitle property for any file in which the DocAuthor is Smith or Jones.


```
SELECT DocTitle
  FROM SCOPE()
  WHERE CONTAINS(DocAuthor,'"Smith" OR "Jones"')
```



The following example searches the contents of all files from the default scope, and retrieves rows consisting of the DocTitle and DocAuthor properties for any file containing the phrases "telecommunications industry" and "United Kingdom".


```
SELECT DocTitle, DocAuthor
  FROM SCOPE()
  WHERE CONTAINS('"telecommunications industry" AND "United Kingdom"')
```



The following example finds documents with, for example, the following contents:

-   "John Doe has always loved ice hockey."
-   "John Doe on Ice: Hockey at Its Best."
-   "Last night, John Doe fell on the ice!! Hockey fans are concerned..."


```
SELECT DocTitle
  FROM SCOPE()
  WHERE CONTAINS('"John Doe" AND "ice hockey"')
```



### Word Prefix Match

A word-prefix match is similar to a simple match, except that the wildcard character asterisk (\*) is used to represent the variable component of a word or phrase. The matching is not case sensitive. Multiple consecutive words are treated as a single phrase, and must appear in exactly the same order in the matching document. If a phrase contains blank spaces between words or punctuation marks, it must be enclosed in double quotes.

``` syntax
CONTAINS ([Column_Reference,]'"Word_or_Phrase*"
          [ Boolean_Operator "Word_or_Phrase"]
           ... ') 
```

### Parameters

<dl> <dt>

<span id="Column_Reference"></span><span id="column_reference"></span><span id="COLUMN_REFERENCE"></span>*Column\_Reference*
</dt> <dd>

Specifies the column name (alias). Its data type must be compatible with the format of the *Word\_or\_Phrase* parameter specified.

</dd> <dt>

<span id="Word_or_Phrase"></span><span id="word_or_phrase"></span><span id="WORD_OR_PHRASE"></span>*Word\_or\_Phrase*
</dt> <dd>

Specifies the literal of type Basic String to use as the prefix.

</dd> <dt>

<span id="Boolean_Operator"></span><span id="boolean_operator"></span><span id="BOOLEAN_OPERATOR"></span>*Boolean\_Operator*
</dt> <dd>

Specifies the Boolean operator to use, following the precedence rules previously stated, that combines the comparison predicates.

</dd> </dl>

### Example

The following example searches the contents of all files from the default scope and retrieves rows for any file that has a DocTitle property consisting of words such as "wine", "winery", "wineries", and so forth.


```
SELECT DocTitle
  FROM SCOPE()
  WHERE CONTAINS('"wine*"')
```



The following example searches the contents of all files from the default scope and retrieves rows for any file that has a DocSubject property containing phrases such as "locating test heaven", "locate tester heaven", "locate tester heavy areas", and so forth.


```
SELECT DocTitle
  FROM SCOPE()
  WHERE CONTAINS(DocSubject,'"locat test heav*"')
```



### Proximity Match

In a proximity match, the query returns a row only if the locations of two or more words in a property are close to each other.

``` syntax
CONTAINS ([Column_Reference,]
          '"Word_or_Phrase" {NEAR | ~}
          "Word_or_Phrase" [{NEAR | ~} "Word_or_Phrase"]
          ... ') 
```

### Parameters

<dl> <dt>

<span id="Column_Reference"></span><span id="column_reference"></span><span id="COLUMN_REFERENCE"></span>*Column\_Reference*
</dt> <dd>

Specifies the column name (alias). Its data type must be compatible with the format of the specified *Word\_or\_Phrase* parameter.

</dd> <dt>

<span id="Word_or_Phrase"></span><span id="word_or_phrase"></span><span id="WORD_OR_PHRASE"></span>*Word\_or\_Phrase*
</dt> <dd>

Specifies the literal of type Basic String to match.

</dd> <dt>

<span id="NEAR____"></span><span id="near____"></span>**NEAR** \| **~**
</dt> <dd>

Specifies the proximity relationship between adjacent words or phrases. (You can also use the tilde (**~**) instead of **NEAR**.) Currently, **NEAR** uses words as the unit of measurement and a value of approximately 50 words as the proximity distance; therefore, if the two phrases are within approximately 50 words, a row is returned.

</dd> </dl>

### Remarks

Index Server 1.x and 2.0 required a parenthesis pair after the **NEAR** operator; for example, **NEAR( )**. Beginning with Indexing Service 3.0, the parenthesis pair is neither required nor recommended, but is supported for backward compatibility.

You can also use a proximity match to query for more than two words that are near each other.

### Examples

The following example returns files where *wordA* is near *wordB*, which is near *wordC*.


```
... WHERE CONTAINS ('"wordA" NEAR "wordB" NEAR "wordC"')
```



The following example returns files where *Indexing* is within approximately 50 words of the word *Service*:


```
... WHERE CONTAINS(DocSubject,'"Indexing" ~ "Services"')
```



The following example returns files containing the word *Microsoft*, and where the word *Indexing* is close to the word *Service*:


```
... WHERE CONTAINS(DocSubject,'"Microsoft" AND "Indexing" NEAR "Service"') 
```



### Linguistic Generation Match

A linguistic generation match is a type of fuzzy search in which the target of the search is expanded to include variations of the word. Currently, the SQL extensions support inflectional morphology generation, in which the search expands to include verb tenses, and the singular or plural of nouns.

``` syntax
CONTAINS ([Column_Reference,]
          'FORMSOF(INFLECTIONAL, "Generation_Term")') 
```

### Parameters

<dl> <dt>

<span id="Column_Reference"></span><span id="column_reference"></span><span id="COLUMN_REFERENCE"></span>*Column\_Reference*
</dt> <dd>

Specifies the column name (alias). Its data type must be compatible with the format of the *Word\_or\_Phrase* parameter specified.

</dd> <dt>

<span id="Generation_Term"></span><span id="generation_term"></span><span id="GENERATION_TERM"></span>*Generation\_Term*
</dt> <dd>

Specifies the literal of type Basic String to expand.

</dd> </dl>

### Example

The following example returns files that contain words such as "driving", "driven", and "drives".


```
... WHERE CONTAINS('FORMSOF(INFLECTIONAL, "drive")')
```



### Weighted Match

The SQL extensions support queries based on matching a group of words or phrases. Also called *vector space queries*, these queries work by weighting each of the match terms, or vector components. The rank of each returned row indicates how well it matches the query. Rows returned do not have to match every listed word or phrase. The matching algorithm uses all the weighted components together when determining a match.

``` syntax
<b>CONTAINS (</b>[<i>Column_Reference</i><b>,</b> ]
          <b>'ISABOUT(</b><i>Vector_Term</i> [<b>WEIGHT(</b><i>Value</i><b>)</b>] [<b>,</b><i>Vector_Term</i> [<b>WEIGHT(</b><i>Value</i><b>)</b>]]
          ...<b>')</b> 
```

### Parameters

<dl> <dt>

<span id="Column_Reference"></span><span id="column_reference"></span><span id="COLUMN_REFERENCE"></span>*Column\_Reference*
</dt> <dd>

Specifies the column name (alias). Its data type must be compatible with the format of the *Vector\_Term* parameter specified.

</dd> <dt>

<span id="Vector_Term"></span><span id="vector_term"></span><span id="VECTOR_TERM"></span>*Vector\_Term*
</dt> <dd>

Specifies the terms to match. The term is one of the following types: Simple, Word Prefix, Proximity, or Linguistic Generation.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>*Value*
</dt> <dd>

Specifies the weight of the *Vector\_Term* parameter. If you specify a weight for a term, you must enclose the term in double quotes. You can specify *Value* in the range of 0.0 to 1.0.

</dd> </dl>

### Example

The following example queries the Contents property for the words "railroad", "transportation", and "locomotive". Files whose Contents include the word "heavy" near the word "locomotive" will be weighted higher in the results ranking. Since the term "transportation" is ranked lower than the other two terms, files containing only that term are ranked lower than files containing either "railroad" or "locomotive".


```
... WHERE CONTAINS
      ('ISABOUT (railroad, "transportation" WEIGHT(0.5),
        "heavy near locomotive" WEIGHT(0.9))')
```



## Related topics

<dl> <dt>

[ARRAY Predicate](array-predicate.md)
</dt> <dt>

[Comparison Predicate](comparison-predicate.md)
</dt> <dt>

[FREETEXT Predicate](freetext-predicate.md)
</dt> <dt>

[LIKE Predicate](like-predicate.md)
</dt> <dt>

[MATCHES Predicate](matches-predicate.md)
</dt> <dt>

[NULL Predicate](null-predicate.md)
</dt> <dt>

[WHERE Clause](where-clause.md)
</dt> </dl>

 

 




