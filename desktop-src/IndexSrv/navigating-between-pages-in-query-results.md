---
Description: Navigating Between Pages in Query Results
ms.assetid: c2e7cf38-1409-4313-a14e-737acbc92e69
title: Navigating Between Pages in Query Results
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Navigating Between Pages in Query Results

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The first record on a page is identified in the variable [CiBookmark](https://www.bing.com/search?q=CiBookmark), which can be used in a form to get to the next page or the previous page. The form variable [CiBookmarkSkipCount](https://www.bing.com/search?q=CiBookmarkSkipCount) should be used with CiBookmark to specify the relative offset from the current page. CiBookmarkSkipCount is typically set to either &lt;%CiMaxRecordsPerPage%&gt; or &lt;%CiMaxRecordsPerPage%&gt;, although it could be set to other multiples of [CiMaxRecordsPerPage](https://www.bing.com/search?q=CiMaxRecordsPerPage).

Here is an example of a form that will skip to the next page for a sequential query:


```
     <FORM ACTION="<%HTTP_SCRIPT_NAME%>?" METHOD="POST">
      <INPUT TYPE="HIDDEN"
             NAME="CiBookmark"
             VALUE="<%CiBookmark%>" >
      <INPUT TYPE="HIDDEN"
             NAME="CiBookmarkSkipCount"
             VALUE="<%CiMaxRecordsPerPage%>" >
      <INPUT TYPE="HIDDEN"
             NAME="CiMaxRecordsPerPage"
             VALUE="<%CiMaxRecordsPerPage%>" >
      <INPUT TYPE="HIDDEN"
             NAME="CiRestriction"
             VALUE="<%CiRestriction%>" >
      <INPUT TYPE="HIDDEN"
             NAME="CiScope"
             VALUE="<%CiScope%>" >
      <INPUT TYPE="SUBMIT" VALUE="Next page">
    </FORM>
```



The following example shows how the buttons for going to adjacent pages can be generated conditionally depending upon the variables [CiContainsFirstRecord](https://www.bing.com/search?q=CiContainsFirstRecord) and [CiContainsLastRecord](https://www.bing.com/search?q=CiContainsLastRecord). It also shows how the number of hits on the next page can be displayed for a nonsequential query.


```
<TABLE> <TR>
    <TD> <%if CiContainsFirstRecord eq 0%>  
     <FORM ACTION="<%HTTP_SCRIPT_NAME%>?" METHOD="POST">
        <INPUT TYPE="HIDDEN"
               NAME="CiBookmark"
               VALUE="<%CiBookmark%>" >
        <INPUT TYPE="HIDDEN"
               NAME="CiBookmarkSkipCount"
               VALUE="-<%CiMaxRecordsPerPage%>" >
        <INPUT TYPE="HIDDEN"
               NAME="CiMaxRecordsPerPage"
               VALUE="<%CiMaxRecordsPerPage%>" >
        <INPUT TYPE="HIDDEN"
               NAME="CiRestriction"
               VALUE="<%CiRestriction%>" >
        <INPUT TYPE="HIDDEN"
               NAME="CiScope"
               VALUE="<%CiScope%>" >
        <INPUT TYPE="SUBMIT" VALUE="Previous <%CiMaxRecordsPerPage%> Hits">
      </FORM>
    <%endif%> </TD>
    <TD> <%if CiContainsLastRecord eq 0%>  
     <FORM ACTION="<%HTTP_SCRIPT_NAME%>?" METHOD="POST">
        <INPUT TYPE="HIDDEN"
               NAME="CiBookmark"
               VALUE="<CiBookmark%>" >
        <INPUT TYPE="HIDDEN"
               NAME="CiBookmarkSkipCount"
               VALUE="<%CiMaxRecordsPerPage%>" >
        <INPUT TYPE="HIDDEN"
               NAME="CiMaxRecordsPerPage"
               VALUE="<%CiMaxRecordsPerPage%>" >
        <INPUT TYPE="HIDDEN"
               NAME="CiRestriction"
               VALUE="<%CiRestriction%>" >
        <INPUT TYPE="HIDDEN"
               NAME="CiScope"
               VALUE="<%CiScope%>" >
        <INPUT TYPE="SUBMIT" VALUE="Next <%CiRecordsOnNextPage%> Hits">
      </FORM>
    <%endif%> </TD>
    </TR> </TABLE> 
```



 

 



