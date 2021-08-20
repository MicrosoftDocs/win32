---
description: Advanced Query Syntax (AQS) is the default query syntax used by Windows Search to query the index and to refine and narrow search parameters.
ms.assetid: 76e33903-d063-48c0-9afe-912c3daa8237
title: Using Advanced Query Syntax Programmatically
ms.topic: article
ms.date: 05/31/2018
---

# Using Advanced Query Syntax Programmatically

Advanced Query Syntax (AQS) is the default query syntax used by Windows Search to query the index and to refine and narrow search parameters. AQS is employed by developers to build queries programmatically (and by users to narrow their search parameters). Canonical AQS was introduced in Windows 7 and must be used in Windows 7 and later to programmatically generate AQS queries.

This topic is organized as follows:

-   [About Advanced Query Syntax](#about-advanced-query-syntax)
    -   [Examples](#examples)
    -   [Properties](#properties)
-   [Keyword Use in Local Languages](#keyword-use-in-local-languages)
-   [Canonical Advanced Query Syntax in Windows 7](#canonical-advanced-query-syntax-in-windows-7)
    -   [Examples](#examples)
    -   [Query Operators](#query-operators)
    -   [Query Values](#query-values)
-   [Scope Restrictions](#scope-restrictions)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## About Advanced Query Syntax

A query consists of basic queries connected with AND, OR, and NOT, as shown in the following example syntax:

``` syntax
<query> ::=
     <basic query>
| ( <query> )
| <query> AND <query>  
| <query> <query>    // Same as <query> AND <query>
| <query> OR <query> 
| NOT <query>
```

> [!Note]  
> AQS is not case sensitive, with the exception of AND, OR, and NOT, which must be in all uppercase.

 

If a query has two or more uses of AND or OR, they will bind from left to right, regardless of whether it is AND or OR. That is, the query, "apple AND pear OR plum" will be interpreted as if it were written as "(apple AND pear) OR plum", and the query, "apple OR pear AND plum", will be interpreted as if it were written as "(apple OR pear) AND plum". So if a document contains the word plum but neither apple, nor pear, the first query will return it but the second query will not. Hence, we recommend that you use explicit parentheses for any query that mixes AND and OR to avoid mistakes or misinterpretations.

A basic query searches for items that satisfy a restriction over a property. The only required portion of a basic query is the restriction or search value. If you do not specify a property, Windows Search searches all properties. <restr> represents the search restriction.

The following forms for a basic query are valid:

``` syntax
<basic query> ::=
     <prop>:<basic restr>
| <restr>
```

A property is designated by a keyword such as author or size, or by a canonical property name such as [System.DateModified](../properties/props-system-datemodified.md). Valid forms for a property are as follows:

``` syntax
<prop> ::= 
     <canonical property name>
| <property label in UI language>
```

An operator indicates an operation such as < or =. For a list of valid operators, see the Query Operators section later in this topic.

A basic restriction is a simple restriction on a property that can be written without parentheses:

``` syntax
<basic restr> ::=
     <value>
| <op><value>
| NOT <basic restr>
| ( <restr> )
```

A restriction is a search value such as a number value or string value, optionally with an operator. Valid forms for a restriction are as follows:

``` syntax
<restr> ::=
    <basic restr>
| <restr> AND <restr>
| <restr> <restr>      // Same as <restr> AND <restr>
| <restr> OR <restr>
```

If you do not specify an operator, Windows Search chooses the most appropriate operator for your query:

-   For a string property, the COP\_WORD\_STARTSWITH $< operator is assumed.
-   For all other properties, the COP\_EQUAL = operator is assumed.

For the programmatic use of AQS, we recommend that you always have an explicit operator. The valid form for searching a simple value or value range is as follows:

``` syntax
<value> ::=
    <simplevalue>
| <simplevalue> .. <simplevalue>
```

A simple value can consist of any of the following types:

``` syntax
<simplevalue> ::=
  []         // No value, or a null value
| <word>     // A sequence of characters without whitespace
| <number>   // An integer or a floating point number
| <datetime> // A relative date, or an absolute date and/or time
| <Boolean>
| "..."      // A phrase
| <enumeration range>
```

### Examples

A query that searches for a document containing the phase "last quarter," authored by Theresa or Lee, and that was saved to the folder MyDocs, combines three basic queries as follows:

``` syntax
"last quarter" author:(theresa OR lee) folder:MyDocs
```

The three basic queries are:

-   "last quarter"
-   author:(theresa OR lee)
-   folder:MyDocs

A basic query that uses canonical syntax is:

``` syntax
System.Size:>1kb
```

### Properties

Properties are referred to by a keyword, which can be a canonical property name in Windows 7 and later. AQS in the Windows UI can use the label instead of the canonical property name, such as author instead of [System.Author](../properties/props-system-author.md). In Windows Vista and earlier it was possible to use English labels regardless of the UI language. In Windows 7 and later, Windows Search recognizes keywords in the current default UI language only.

### Support for Custom Properties

In Windows Vista and earlier, custom properties were not available in AQS. In Windows 7 and later, AQS works with custom properties that are registered with the property system. For more information on creating custom properties, see [Property System](../properties/building-property-handlers.md).

### DateTime properties in Windows 8

As of Windows 8, DateTime properties (like [System.DateModified](../properties/props-system-datemodified.md)) support the canonical date and time format specified by [ISO-8601](https://www.w3.org/TR/NOTE-datetime), optionally including the UTC time zone.

-   **Windows 8 and earlier, date-time without UTC time zone:** *YYYY*-*MM*-*DDThh*:*mm*:*ss*

    This format specifies a local time, regardless of the user or system locale.

-   **Windows 8, date-time with UTC time zone:** *YYYY*-*MM*-*DDThh*:*mm*:*ssTZD*

    This format specifies a time at the specified UTC time zone.

## Keyword Use in Local Languages

In Windows 7 and later, mnemonic keywords work in the system language only, such as German keywords only on a German operating system, and English keywords only on an English operating system. [System.Author](../properties/props-system-author.md) is a canonical keyword, and the mnemonic value for the System.Author property is Author, for example. The introduction of canonical keywords compensates for the fact that English mnemonic keywords are no longer universally recognized on all operating systems regardless of language, as was the case in Windows Vista and earlier.

> [!Note]  
> In Windows 7 and later, Windows Search recognizes keywords in the current default language only, and not in English unless English is the current default. We recommend that developers always use canonical syntax so that their application won't have language problems with keywords.

 

## Canonical Advanced Query Syntax in Windows 7

Canonical syntax was introduced for keywords in Windows 7. An example of a query with a canonical property is `System.Message.FromAddress:=me@microsoft.com`. When coding queries in applications running on Windows 7 and later, you must use canonical syntax to programmatically generate AQS queries. If you do not use canonical syntax and your application is deployed in a locale or UI language different from the language in the application code, your queries will not be interpreted correctly.

The conventions for canonical keyword syntax are as follows:

-   The canonical syntax for a property is its canonical name, such as `System.Photo.LightSource`. Canonical names are not case sensitive.
-   The canonical syntax for the Boolean operators consists of the keywords AND, OR, and NOT, in all uppercase.
-   The operators <, >, =, and so forth, are not localized and are thus also part of the canonical syntax.
-   If a property `P` has enumerated values or ranges named N₁ through Nₖ, the canonical syntax for the *I*th value or range is the canonical name for P, followed by the character \#, followed by N<sub>I</sub>, as illustrated in the following example:
    -   `System.Photo.LightSource#Daylight`, `System.Photo.LightSource#StandardA`, and so forth.
-   For a defined semantic type T with values or ranges named N₁ through Nₖ, the canonical syntax for the *I*th value or range is the canonical name for T, followed by the character \#, followed by N<sub>I</sub>, as illustrated in the following example:
    -   `System.Devices.LaunchDeviceStageFromExplorer:=System.StructuredQueryType.Boolean#True`
-   For literal values such as words or phrases, the canonical syntax is the same as the regular syntax. Examples of queries with literal values in canonical syntax are:
    -   `System.Author:sanjay`
    -   `System.Keywords:"Animal"`
    -   `System.FileCount:>100`

> [!Note]  
> There is no canonical syntax for numbers in Windows 7 and later. Because floating point formats vary among locales, the use of a canonical query that involves a floating point constant is not supported. Integer constants, in contrast, can be written using only digits (no separators for thousands) and can be safely used in canonical queries in Windows 7 and later.

 

### Examples

The following table shows some examples of canonical properties and the syntax for using them.



| Type of canonical property | Example                                                                                     | Syntax                                                                                                                                                                                                                                                  |
|----------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| String value               | [System.Author](../properties/props-system-author.md)<br/>    | The string value is searched for in the author property: <br/>`System.Author:Jacobs`                                                                                                                                                              |
| Enumeration range          | [System.Priority](../properties/props-system-priority.md)             | The priority property can have a numerical value range:<br/>`System.Priority:System.Priority#High`                                                                                                                                                |
| Boolean                    | [System.IsDeleted](../properties/props-system-isdeleted.md)<br/> | Boolean values can be used with any Boolean property:<br/>`System.IsDeleted:System.StructuredQueryType.Boolean#True`, and `System.IsDeleted:System.StructuredQueryType.Boolean#False`                                                             |
| Numerical                  | [System.Size](../properties/props-system-size.md)<br/>      | It is not possible to write safely a canonical query that involves a floating point constant, because floating point formats vary among locales. Integers must be written with no separators for thousands. For example:<br/>`System.Size:<12345` |



 

For more information about canonical properties and the property system generally, see [System Properties](../properties/props.md). Alternatively, refer to the public header files.

### Query Operators

If a property, p, has multiple values for some item, an AQS query for p:<restr> returns the item if <restr> is **true** for at least one of the values. (<restr> represents a restriction.)

The syntax listed in the following table consists of an operator, operator symbol, example and example description. The operator and symbol can be used in any language and included in any query. Do not use the COP\_IMPLICIT or COP\_APPLICATION\_SPECIFIC operators. Some of the operators have interchangeable symbols.



<table>
<colgroup>
<col  />
<col  />
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Operator</th>
<th>Symbol</th>
<th>Example</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>COP_EQUAL</td>
<td>=<br/></td>
<td>System.FileExtension:=&quot;.txt&quot;<br/></td>
<td>The value is the string &quot;<em>.txt</em>&quot;.<br/></td>
</tr>
<tr class="even">
<td>COP_NOTEQUAL</td>
<td>≠<br/> -<br/> &lt;&gt;<br/> NOT<br/> - -<br/></td>
<td>System.Kind:≠picture<br/> System.Photo.DateTaken:-[]¹<br/> System.Kind:&lt;&gt;picture<br/> System.Kind:NOT picture<br/> System.Kind:- -picture<br/></td>
<td>The <a href="/windows/desktop/properties/props-system-kind">System.Kind</a> property is not a picture.<br/> The <a href="/windows/desktop/properties/props-system-photo-datetaken">System.Photo.DateTaken</a> property has a value.<br/> The <a href="/windows/desktop/properties/props-system-kind">System.Kind</a> property is not a picture. <br/> The <a href="/windows/desktop/properties/props-system-kind">System.Kind</a> property is not a picture. <br/> Double NOT operators applied to the same property do not cancel out. Hence, System.Kind:- -picture is equivalent to System.Kind:-picture and System.Kind:NOT picture.<br/></td>
</tr>
<tr class="odd">
<td>COP_LESSTHAN</td>
<td>&lt;<br/></td>
<td>System.Size:&lt;1kb<br/></td>
<td>This value is less than <em>1kb</em>.<br/></td>
</tr>
<tr class="even">
<td>COP_GREATERTHAN</td>
<td>&gt;<br/></td>
<td>System.ItemDate:&gt;System.StructuredQueryType.DateTime#Today<br/></td>
<td>This value is greater than <em>today</em>.<br/></td>
</tr>
<tr class="odd">
<td>COP_LESSTHANOREQUAL</td>
<td>&lt;=<br/> ≤<br/></td>
<td>System.Size:&lt;=1kb<br/></td>
<td>This value is less than or equal to <em>1kb</em>.<br/></td>
</tr>
<tr class="even">
<td>COP_GREATERTHANOREQUAL</td>
<td>&gt;=<br/> ≥<br/></td>
<td>System.Size:&gt;=1kb<br/></td>
<td>This value is equal to or greater than <em>1kb</em>.<br/></td>
</tr>
<tr class="odd">
<td>COP_VALUE_STARTSWITH</td>
<td>~&lt;<br/></td>
<td>System.FileName:~&lt;&quot;C++ Primer&quot;<br/></td>
<td>Finds items where the file name begins with the characters &quot;<em>C++ Primer</em>&quot;.<br/></td>
</tr>
<tr class="even">
<td>COP_VALUE_ENDSWITH</td>
<td>~&gt;<br/></td>
<td>System.Photo.CameraModel:~&gt;non<br/></td>
<td>Finds items where the property value ends with the characters <em>non</em>.<br/></td>
</tr>
<tr class="odd">
<td>COP_VALUE_CONTAINS</td>
<td>~=<br/> ~~<br/></td>
<td>System.Subject.~=round <br/> System.Search.Autosummary:~~round<br/></td>
<td>Finds a message that has this string in the subject, and will match &quot;g<em>round</em> rules&quot; for example.<br/> Finds all items with an Autosummary that contains the characters <em>round</em>.<br/></td>
</tr>
<tr class="even">
<td>COP_VALUE_NOTCONTAINS</td>
<td>~!<br/></td>
<td>System.Author:~!&quot;sanjay&quot;<br/></td>
<td>Finds authors that do not have the character sequence&quot;<em>sanjay</em>&quot; in them.<br/></td>
</tr>
<tr class="odd">
<td>COP_DOSWILDCARDS</td>
<td>~ <br/></td>
<td>System.FileName:~&quot;Mic?osoft W*d&quot;<br/></td>
<td>Finds files where the file name starts with <em>Mic</em>, followed by some character, followed by <em>osoft w</em>, followed by any characters ending with <em>d</em>. <br/> The ? and * characters are not interpreted literally, and work like DOS-style wildcard characters:<br/>
<ul>
<li>? matches one arbitrary character.</li>
<li>* matches zero or more arbitrary characters.</li>
</ul></td>
</tr>
<tr class="even">
<td>COP_WORD_EQUAL</td>
<td>$=<br/> $$<br/></td>
<td>System.StructuredQuery.Virtual.From:$=&quot;Sanjay Jacobs&quot;<br/></td>
<td>For Windows 7 and later. Finds the phrase &quot;<em>Sanjay Jacobs</em>&quot; in all From properties. The word <em>Sanjay</em> must be followed by the word <em>Jacobs</em>.<br/></td>
</tr>
<tr class="odd">
<td>COP_WORD_STARTSWITH</td>
<td>$<<br/></td>
<td>System.Author:$<&quot;San&quot; System.Filename:$<&quot;Micro Exe&quot;<br/></td>
<td>For Windows 7 and later. Finds any item where Author contains a word starting with the characters &quot;<em>San</em>&quot;.<br/> Finds any file in which the file name contains a word starting with <em>micro</em>, followed by a word starting with <em>exe</em>.<br/></td>
</tr>
</tbody>
</table>



 

¹ Empty square brackets (\[\]) denote "no value".

For string properties the default operation is either COP\_WORD\_STARTS\_WITH or COP\_WORD\_EQUAL.

### Query Values

Useful examples of how query values can be restricted are listed in the following table.



<table>
<colgroup>
<col  />
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Value/symbol</th>
<th>Examples</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>String</td>
<td>auto<br/></td>
<td>Any sequence of characters that can be searched for. The string must not contain whitespace or character combinations that are part of the syntax. This example searches for a word beginning with <em>auto</em>.<br/></td>
</tr>
<tr class="even">
<td>Quoted string &quot;&quot;</td>
<td>&quot;Conclusions: valid&quot; &quot;The &quot;&quot;blue&quot;&quot; team&quot;<br/></td>
<td>Any sequence of characters. The string is not interpreted as part of the syntax.<br/> Quotation marks can be included in a query if they are doubled. This example searches for <em>The &quot;blue&quot; team</em>.<br/></td>
</tr>
<tr class="odd">
<td>Integer</td>
<td>5678<br/></td>
<td>Use only digits for integers. Do not use any separators for thousands.<br/></td>
</tr>
<tr class="even">
<td>Floating point number</td>
<td>5678.1234<br/></td>
<td>Because floating point formats vary among locales, a canonical query cannot use a floating point constant. The use of canonical syntax with floating point numbers is not localization safe. <br/></td>
</tr>
<tr class="odd">
<td>Boolean <strong>true</strong>/<strong>false</strong></td>
<td>System.IsRead:=System.StructuredQueryType.Boolean#True<br/> System.IsEncrypted:-System.StructuredQueryType.Boolean#False<br/></td>
<td>The <strong>TRUE</strong> Boolean value.<br/> The <strong>FALSE</strong> Boolean value.<br/></td>
</tr>
<tr class="even">
<td>[]</td>
<td>System.Keywords:=[]<br/></td>
<td>Empty square brackets denote that there is no value. This example finds all items that have not been tagged. <br/></td>
</tr>
<tr class="odd">
<td>Absolute dates</td>
<td>System.ItemDate:1/26/2010<br/> SystemDateModified 10/15/2002 19:00<br/></td>
<td>Finds items with a date of 26 January 2010.<br/> Finds items that were modified on 15 October 2002 between the hours 19:00:00 and 19:00:59. <br/>
<blockquote>
[!Note]<br />
Because date formats (like floating point formats) vary among locales, the use of canonical syntax with absolute dates is not supported and is not localization safe.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>Relative dates</td>
<td>System.ItemDate:System.StructuredQueryType.DateTime#Today<br/> System.DateAcquired:System.StructuredQueryType.DateTime#NextMonth<br/> System.Message.DateReceived:System.StructuredQueryType.DateTime#LastYear<br/></td>
<td>Finds items with today's date.<br/> Finds items with a date in the next month.<br/> Finds items with a date in the last year.<br/>
<blockquote>
[!Note]<br />
In addition to searching on specific dates and date ranges, AQS recognizes relative date values (like <em>today</em>, <em>tomorrow</em>, <em>nextweek</em>, <em>nextmonth</em>), and day (like <em>Tuesday</em> or <em>Monday..Wednesday</em>), and month (<em>February</em>).
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>..</td>
<td>System.ItemDate:11/05/04..11/10/04 System.Size:5kb..10kb<br/></td>
<td>Double periods indicate a value range. Finds items with a date between 11/05/04 and 11/10/04, inclusive.<br/> Finds items between 5 and 10kb in size.<br/></td>
</tr>
</tbody>
</table>



 

## Scope Restrictions

Users can limit the scope of their searches to specific folder locations or data stores. For example, if you use several email accounts and you want to limit a query to either Microsoft Outlook or Microsoft Outlook Express, you can use `System.Search.Store:mapi` or `System.Search.Store:oe` respectively. The following table shows some examples of how to restrict a search by data store.



| Restrict search by data store  | Keyword | Example                                     |
|--------------------------------|---------|---------------------------------------------|
| Files                          | file    | System.Search.Store:file                    |
| Outlook                        | mapi    | System.Search.Store:mapi                    |
| Outlook Express                | oe      | System.Search.Store:oe                      |
| Offline files                  | csc     | System.Search.Store:csc                     |
| Specific folder on local drive | folder  | System.ItemFolderNameDisplay:C:"\\MyFolder" |



 

## Additional Resources

-   In Windows 7 and later, a shortcut menu option can be available based on whether an AQS condition is met. For more information, see "Getting Dynamic Behavior for Static Verbs by Using Advanced Query Syntax" in [Creating Context Menu Handlers](../shell/context-menu-handlers.md).
-   AQS queries can be limited to specific types of files, which are known as file kinds. For more information, see [File Types and Associations](../shell/fa-intro.md). For property reference documentation, see [System.Kind](../properties/props-system-kind.md), and [System.KindText](../properties/props-system-kindtext.md).

## Related topics

<dl> <dt>

[Querying the Index Programmatically](-search-3x-wds-qryidx-overview.md)
</dt> <dt>

[Using SQL and AQS Approaches to Query the Index](-search-3x-wds-qryidx-overview.md)
</dt> <dt>

[Querying the Index with ISearchQueryHelper](-search-3x-wds-qryidx-searchqueryhelper.md)
</dt> <dt>

[Querying the Index with the search-ms Protocol](-search-3x-wds-qryidx-searchms.md)
</dt> <dt>

[Querying the Index with Windows Search SQL Syntax](-search-sql-windowssearch-entry.md)
</dt> </dl>

 

 
