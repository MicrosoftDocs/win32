---
title: Maintaining Session Information
description: Maintaining Session Information
ms.assetid: 2ab862dc-62e1-44d6-ac81-7d3c574a779f
keywords:
- Windows Media Player online stores,Download Manager
- online stores,Download Manager
- type 2 online stores,Download Manager
- Windows Media Player online stores,maintaining session information
- online stores,maintaining session information
- type 2 online stores,maintaining session information
- Windows Media Player online stores,session information
- online stores,session information
- type 2 online stores,session information
- Windows Media Player,Download Manager
- Windows Media Player Download Manager
- Download Manager
- maintaining session information
- session information
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Maintaining Session Information

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## How the Sample Stores Information

The sample webpage maintains data by using cookies. Cookies are simply persistent name/value pairs that the Web browser can store for you.

When the webpage closes, the **Shutdown** function runs. **Shutdown** calls the function **SetPendingCookies**. This function loops through the download collection list, stored in the drop-down list box named selDLC. If a download collection contains incomplete items, the function calls the method **SetCookie**, passing a name and a value. The name string is determined by appending an integer value to a constant value, **WMPDLC**, which is stored in the variable named g\_sPreCookie. For instance, for the third pending download collection, the cookie name would be "WMPDLC2", because the counting mechanism is zero-based. As each cookie is created, the function increments the global variable g\_Pending to keep a count of pending downloads. The code is reproduced here for your convenience:


```C++
// Write cookies for pending downloads.
function SetPendingCookies()
{
    g_Pending = 0; // Init the pending count.
    
    for(var i = 0; i < selDLC.length; i++)
    {
        var sCookieName = g_sPreCookie + i.toString(10);
        var sCookieVal = selDLC.options[i].text;
    
        // Write a cookie for each pending download.    
        if(IsDLCComplete(sCookieVal.valueOf()) == false)
        {      
            SetCookie(sCookieName, sCookieVal);
            g_Pending++;
        }        
    }
}

```



**IsDLCComplete** is a helper function that simply loops through each download item in the download collection to determine whether any item is pending. If there is a pending item, the function returns false.

**SetCookie** is the function that creates the cookie.

When **SetPendingCookies** returns, **Shutdown** creates the count cookie, which stores the value from the variable g\_Pending. This value is important because the webpage needs a way to determine how many cookies to retrieve when it reloads. The count cookie name is stored in the variable named g\_sCountCookie.

## How the Sample Retrieves Information

When the webpage loads, the **Init** function runs. First, the function calls **GetPendingDlCount** to retrieve the count cookie. Next, it stores this value in the variable named g\_Pending. Then it calls the **PopulateDLList** function to retrieve each download session cookie and add its identifier to the drop-down list box. Here is the code for that function:


```C++
// Fill the drop-down list with pending download collection IDs.
function PopulateDlList(iCount)
{
    ClearList(selDLC);
     
    // For each cookie, add the value to the SELECT element.
    // The value represents a download collection ID.  
    for (var j = 0; j < iCount; j++)
    {
        var sCookieName = g_sPreCookie + j.toString(10);        
        var sCookieVal = GetCookie(sCookieName);
        DelCookie(sCookieName); // Don't leave the cookies lying around. 
  
        if(sCookieVal != null)
        {      
            var oOption = document.createElement("OPTION");
            oOption.text = sCookieVal;
            oOption.value = j;
            selDLC.add(oOption); 
        }          
    }
}

```



The function **ClearList** removes all items from the list box.

The function then enters a loop. Each cookie name is built as a string, and then the cookie is retrieved by calling the helper function **GetCookie**. Once retrieved, the cookie is deleted by calling **DelCookie**. If the cookie has a value, the value is added to the list box. This action initiates the **onChange** event for the selDLC list, which in turn calls the handler function named **OnSelectDLC**. This is the same function that executes when the user selects a download collection; it is the code that fills the download item list box.

## Related topics

<dl> <dt>

[**Using the Download Manager**](using-the-download-manager.md)
</dt> </dl>

 

 




