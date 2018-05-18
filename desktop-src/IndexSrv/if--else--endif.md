---
title: if, else, endif
description: if, else, endif
ms.assetid: '2717f3ca-d578-4e86-bc8b-c4d76022d4db'
---

# if, else, endif

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

HTML extension files can contain conditional logic with an if-then-else statement to control how the webpage is constructed. For example, one common usage is to insert a condition to display a header for the query on the first row within a &lt;%begindetail%&gt; section. If there are no records returned by the query, the HTML extension file displays the text ?Sorry, no authors had YTD sales greater than? %sales%. By using the &lt;%if%&gt; statement and a built-in variable called CiLastRecordNumber, you can tailor the output so that the error message is printed when no records are returned. Here is an example showing the use of the &lt;%if%&gt; statement.


```
<%begindetail%> 
      <%if CiCurrentRecordNumber EQ 1%> 
        Query results:
        <B>Author YTD Sales<BR></B>
      <%endif%> 
      <%au_lname%>$<%ytd_sales%> 
    <%enddetail%> 
    <P>
    <%if CiLastRecordNumber EQ 0%> 
      <I><B>Sorry, no authors had YTD sales greater than </I><%sales%>.</B>
      <P>
    <%else%> 
    <HR>
      <I>
      The webpage you see here was created by merging the results
      of the Content query with the template file Sample.htx.
      <P>
      The merge was done by Indexing Service and
      the results were returned to this Web browser by 
      Internet Information Services (IIS).
      </I>
    <%endif%> 
    </BODY>
    </HTML>
```



The general syntax is:

``` syntax
<%if condition%> 
    HTML text
    [ <%else%> 
      HTML text ]
    <%endif%>
```

where the condition is of the form *value1* *operator* *value2* and *operator* can be one of the following:

<dl> <dt>

<span id="EQ"></span><span id="eq"></span>EQ
</dt> <dd>

if *value1* equals *value2*

</dd> <dt>

<span id="NE"></span><span id="ne"></span>NE
</dt> <dd>

if *value1* does not equal *value2*

</dd> <dt>

<span id="LT"></span><span id="lt"></span>LT
</dt> <dd>

if *value1* is less than *value2*

</dd> <dt>

<span id="LE"></span><span id="le"></span>LE
</dt> <dd>

if *value1* is less than or equal to *value2*

</dd> <dt>

<span id="GT"></span><span id="gt"></span>GT
</dt> <dd>

if *value1* is greater than *value2*

</dd> <dt>

<span id="GE"></span><span id="ge"></span>GE
</dt> <dd>

if *value1* is greater than or equal to *value2*

</dd> <dt>

<span id="CONTAINS"></span><span id="contains"></span>CONTAINS
</dt> <dd>

if any part of *value1* contains the string *value2*

</dd> <dt>

<span id="ISTYPEEQ"></span><span id="istypeeq"></span>ISTYPEEQ
</dt> <dd>

allows the .htx file to determine the **VT\_TYPE** of a particular variable.

value1 IsTypeEq value2 value1 IsTypeEq const1 const1 IsTypeEq value1

For example, if a variable is of type currency (**VT\_CY**), its type is 6. Type numbers are defined in the ActiveX specification. A valid .htx comparison would be:

``` syntax
<%if propName IsTypeEq 6%>Variable is of type currency
<%else%>Variable is NOT type currency
<%endif%> 
```

This operator is especially useful to check for type **VT\_EMPTY**, an empty property.

</dd> <dt>

<span id="ISEMPTY"></span><span id="isempty"></span>ISEMPTY
</dt> <dd>

TRUE if value1 is of type **VT\_EMPTY**, or of type **VT\_NULL**, or is of a textual type (**VT\_LPSTR**, **VT\_LPWSTR**, **VT\_BSTR**, or vectors of the preceding types) and contains only ?empty? characters (space, tab, and so on.)

</dd> </dl>

The operands *value1* and *value2* can be column names, one of the built-in variables, an HTTP variable name (see [HTTP Variables](http-variables.md)), or a constant. When used in an &lt;%if%&gt; statement, values are not delimited with &lt;% and %&gt;. For example, to do special processing on author name ?Green,? use the condition:

``` syntax
<FORM ACTION="<%HTTP_SCRIPT_NAME%>?" METHOD="POST">
      <%if au_lname EQ "Green"%> 
        this guy is green!
      <%endif%> 
    <%enddetail%>
```

The &lt;%if%&gt; statement can also be used to do special processing based on information from HTTP variables. For example, to format a page differently for a different type of client Web browser (in this case, Netscape Navigator), you could include the following in the HTML extension file.

``` syntax
<%if HTTP_USER_AGENT contains "Mozilla"%> 
      client supports advanced HTML features
    <%else%> 
      client is <%HTTP_USER_AGENT%> 
    <%endif%>
```

Property types **VT\_FILETIME** and **VT\_DATE** can be compared within &lt;%if%&gt; statements. Use the following format:

``` syntax
<%if fileTime eq "yyyy/mm/dd hh:mm:ss:iii"%>File times are identical
<%endif%>
```

The time must be enclosed in quotes. The year must be a four-digit number (for example, 1996, not 96), and slashes and colons are required.

yyyy = year

mm = month ( 1=January, 12=December, and so on)

dd = day of month ( 1 - 31)

hh = hour of the day in 24-hour format (optional)

mm = minutes (optional)

ss = seconds (optional)

iii = milliseconds (optional)

For example:

``` syntax
<%if write le "1996/07/21 17:22:11:333"%>File times are identical
<%endif%>
```

 

 




