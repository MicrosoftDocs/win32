---
title: Navigating between Service Task Panes
description: Navigating between Service Task Panes
ms.assetid: cb26a26d-a80d-4af5-9c5f-fab01129d83c
keywords:
- Windows Media Player online stores,navigating
- online stores,navigating
- type 2 online stores,navigating
- Windows Media Player online stores,service task panes
- online stores,service task panes
- type 2 online stores,service task panes
- Windows Media Player online stores,task panes
- online stores,task panes
- type 2 online stores,task panes
- navigating type 2 online stores
- Windows Media Player,service task panes
- Windows Media Player,task panes
- service task panes
ms.topic: article
ms.date: 05/31/2018
---

# Navigating between Service Task Panes

To navigate between service task panes in Windows Media Player, you use the **NavigateTaskPaneURL** method, which is available by using the **window.external** object. When you use this method, you specify values for three parameters:

-   *bstrKeyName*. This is the key name of the online store. When navigating within an online store, use the key name of the current store.
-   *bstrTaskPane*. This string contains the name of the service task pane to which you want to navigate.
-   *bstrParams*. This string contains the query string parameters you want to append to the URL for the webpage hosted by the service task pane to which you want to navigate.

Navigation is managed by a webpage you create, called the navigate page. The URL for the navigate page is specified by the **Navigate** element in the ServiceInfo document. When you call **NavigateTaskPaneURL**, Windows Media Player opens the navigate page, not the webpage specified by the **ServiceTask1**, **ServiceTask2**, or **ServiceTask3** elements. It is the navigate page that receives the query string specified by *bstrParams*. The navigate page should contain the rules that determine which content displays in a service task pane after navigation.

For example, suppose you want users to click a link to navigate from **ServiceTask1** to **ServiceTask2**. You could use the following HTML to create the link:


```C++
<A HREF = "javascript:window.external.NavigateTaskPaneURL('MSSampleMusic', 'ServiceTask2', 'From=Music&To=2')">Video</A>

```



When the user clicks the Video link, Windows Media Player switches to **ServiceTask2** and opens the navigate page, appending the following query string to its URL.


```C++
?From=Music&To=2

```



The From parameter identifies the page from which the user clicked the link and the To parameter identifies the number of the service task pane to which he or she wants to navigate. (Note that there is nothing special about these parameters. You can use any parameters you like for any purpose you choose.)

For instance, the following example code shows the **Navigate** element in a ServiceInfo document:


```C++
<Navigate
        BaseURL = "https://www.proseware.com/service/html/navigate.asp">
```



The resulting URL, complete with query string, is shown in the following example:


```C++
https://www.proseware.com/service/html/navigate.asp?From=Music&To=2

```



The following example code shows the navigate page:


```C++
<%
    Dim sURL
    Dim sQS
    Dim sTo

    sURL = ""
    sQS = Request.ServerVariables("QUERY_STRING")
    sTo = "" & Request.QueryString("To")
 
    Select Case sTo
       Case "1" sURL = sURL & "Music_Music.asp"
       Case "2" sURL = sURL & "Music_Video.asp"
       Case "3" sURL = sURL & "Music_Radio.asp"
       Case Else sURL = sURL & "Music_Music.asp"
    End Select
     
    sURL = sURL & "?" & sQS

    Response.Redirect(sURL)    
%>

```



The preceding code simply creates a URL and redirects the browser to it. First, the code retrieves To values from the URL query string and the query string itself. It uses the value of the To parameter to determine which page to display. It then appends the original query string to the URL. Finally, it navigates the browser using a URL similar to the following:


```C++
https://www.proseware.com/service/html/Video.asp?locale=409&geoid=f4&version=10.0.0.3600&userlocale=409&From=Music&To=2

```



Whenever you perform navigation in this manner, be sure to specify [External.SelectedTaskPane](external-selectedtaskpane.md) to ensure that the correct task button is highlighted.

-   **Warning** Be careful how you use query string parameters for navigation.

HTMLView webpages can be provided by anyone who creates an ASX playlist. This means that malicious websites can pass query string values to your online store using **NavigateTaskPaneURL**. You must plan for this possibility to keep your online store secure. For example, if your online store simply displays a query string value to the user, a malicious website could display unexpected text.

## Related topics

<dl> <dt>

[**Displaying Web Pages in Windows Media Player**](displaying-web-pages-in-windows-media-player.md)
</dt> <dt>

[**Navigate Element**](navigate-element.md)
</dt> <dt>

[**Navigation for Type 2 Online Stores**](navigation-for-type-2-online-stores.md)
</dt> </dl>

 

 




