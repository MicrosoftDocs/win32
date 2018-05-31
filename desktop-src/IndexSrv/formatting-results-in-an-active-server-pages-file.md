---
title: Formatting Results in an Active Server Pages File
description: Formatting Results in an Active Server Pages File
ms.assetid: 7ce262a7-84fa-4ef0-8ec9-603ac6557698
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Formatting Results in an Active Server Pages File

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The last part of this example shows how to format your query results. This portion of an .asp file contains variables that determine the information displayed in the results of a search; this is equivalent in function to an .htx file.


```
<%
  if ActiveQuery then
    if not RS.EOF then
 %>
<p>
<HR width="80%" ALIGN=center SIZE=3>
<p>
 
<%
     LastRecordOnPage = NextRecordNumber + RS.PageSize - 1
     CurrentPage = RS.AbsolutePage
     if RS.RecordCount <> -1 AND RS.RecordCount < LastRecordOnPage then
         LastRecordOnPage = RS.RecordCount
     end if
 
     Response.Write "Documents " & NextRecordNumber & " to " & LastRecordOnPage
     if RS.RecordCount <> -1 then
         Response.Write " of " & RS.RecordCount
     end if
     Response.Write " matching the query " & chr(34) & "<I>"
     Response.Write SearchString & "</I>" & chr(34) & ".<P>"
 %>
```



The following section is equivalent to the &lt;%Begindetail%&gt; &lt;%Enddetail%&gt; section in an .htx file.


```
<dl>
 
<!-- BEGIN first row of query results table -->
<% Do While Not RS.EOF and NextRecordNumber <= LastRecordOnPage %>
 
<%
    ' This is the detail portion for Title, Abstract, URL, Size, and
    ' Modification Date.
 
    ' If there is a title, display it, otherwise display the virtual path.
%>
    <p>
    <dt><%= NextRecordNumber%>.
        <%if VarType(RS("DocTitle")) = 1 or RS("DocTitle") = "" then%>
            <b><a href="<%=RS("vpath")%>"><%= Server.HTMLEncode( RS("filename") )%></a></b>
        <%else%>
            <b><a href="<%=RS("vpath")%>"><%= Server.HTMLEncode(RS("DocTitle"))%></a></b>
        <%end if%>
    <dd>
        <%if VarType(RS("characterization")) = 8 and RS("characterization") <> "" then%>
            <b><i>Abstract:  </I></b><%= Server.HTMLEncode(RS("characterization"))%>
            <br>
        <%end if%>
        <cite>
            <a href="<%=RS("vpath")%>">http://<%=Request("server_name")%><%=RS("vpath")%></a>
            <font size=-1> - <%if RS("size") = "" then%>(size and time unknown)<%else%>size <%=RS("size")%> bytes - <%=RS("write")%> GMT<%end if%></font>
        </cite>
 
<%
          RS.MoveNext
          NextRecordNumber = NextRecordNumber+1
      Loop
%>
 
</dl>
```



The section equivalent to the &lt;%BeginDetail%&gt;&lt;%EndDetail%&gt; section in an .htx file ends here. The following section displays information about the query.


```
<P><BR>
 
<%
  else   ' NOT RS.EOF
      if NextRecordNumber = 1 then
          Response.Write "No documents matched the query<P>"
      else
          Response.Write "No more documents in the query<P>"
      end if
 
  end if ' NOT RS.EOF
 %>
 
<!-- If the index is out of date, display the fact -->
 
<%if Q.OutOfDate then%>
    <P>
    <I><B>The index is out of date.</B></I><BR>
<%end if%>
 
<!--
    If the query was not executed because it needed to enumerate to
    resolve the query instead of using the index, but AllowEnumeration
    was FALSE, let the user know
-->
 
<%if Q.QueryIncomplete then%>
    <P>
    <I><B>The query is too expensive to complete.</B></I><BR>
<%end if%>
 
<!--
    If the query took too long to execute (for example, if too much work
    was required to resolve the query), let the user know
-->
 
<%if Q.QueryTimedOut then%>
    <P>
    <I><B>The query took too long to complete.</B></I><BR>
<%end if%>
```



The next portion sets the **Previous** and **Next** navigation buttons when a query returns more results than called for per page. Comments within the code explain each section.


```
<TABLE>
 
<!--
    This is the "previous" button.
    This retrieves the previous page of documents for the query.
-->
 
<%SaveQuery = FALSE%>
<%if CurrentPage > 1 and RS.RecordCount <> -1 then%> 
    <td align=left>
        <form action="<%= QueryForm%>" method="POST">
            <INPUT TYPE="HIDDEN" NAME="SearchString" VALUE="<%=SearchString%>">
            <INPUT TYPE="HIDDEN" name="pg" VALUE="<%=CurrentPage-1%>" >
           
            <input type="submit" value="Previous <%=RS.PageSize%> documents">
        </form>
    </td>
    <%SaveQuery = TRUE%>
<%end if%>
 
<!--
    This is the "next" button.
    This button retrieves the next page of documents for the query.
    If the RS.RecordCount is available, the number of
    documents on the next page will be displayed.
-->
 
<%if Not RS.EOF then%>
    <td align=right>
        <form action="<%= QueryForm%>" method="POST">
            <INPUT TYPE="HIDDEN" NAME="SearchString" VALUE="<%=SearchString%>">
            <INPUT TYPE="HIDDEN" name="pg" VALUE="<%=CurrentPage+1%>" >
 
            <% NextString = "Next "
               if RS.RecordCount <> -1 then
                   NextSet = (RS.RecordCount - NextRecordNumber) + 1
                   if NextSet > RS.PageSize then
                       NextSet = RS.PageSize
                   end if
                   NextString = NextString & NextSet & " documents"
               else
                   NextString = NextString & " page of documents"
               end if
             %>
            <input type="submit" value="<%=NextString%>">
        </form>
    </td>
    <%SaveQuery = TRUE%>
<%end if%>
 
</TABLE>
 
 
<!-- Display the page number -->
 
Page <%=CurrentPage%>
<%if RS.PageCount <> -1 then
     Response.Write " of " & RS.PageCount
  end if %>
```



The next section tells where the *RS* and *Q* variables are stored in the ASP session variables. Storing these variables is convenient for navigation. As an alternative, you can re-execute the query when the user displays another page.


```
<%
    ' If either of the previous or back buttons were displayed, save the query
    ' and the recordset in session variables.
    if SaveQuery then
        set Session("Query") = Q
        set Session("RecordSet") = RS
    else
        RS.close
        Set RS = Nothing
        Set Q = Nothing
        set Session("Query") = Nothing
        set Session("RecordSet") = Nothing
    end if
 %>
<% end if 
 
elseif not NewQuery then
    Response.Write ""
else
    Response.Write "Please enter a word or phrase to search for."
end if
 
%>
```



 

 




