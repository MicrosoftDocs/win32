---
title: Using the Active Desktop Object
description: This article contains information on the ActiveDesktop object that is part of the Windows Shell API. This object, through its IActiveDesktop interface, enables you to add, remove, and change items on the desktop.
ms.assetid: 68d72b0f-f5e9-4fff-bb13-4c60d1dd7009
keywords:
- ActiveDesktop object
- Active Desktop
- enumeration,desktop items
ms.topic: article
ms.date: 05/31/2018
---

# Using the Active Desktop Object

\[This feature is supported only under Windows XP or earlier. \]

This article contains information on the **ActiveDesktop** object that is part of the Windows Shell API. This object, through its [**IActiveDesktop**](https://msdn.microsoft.com/en-us/library/Bb776357(v=VS.85).aspx) interface, enables you to add, remove, and change items on the desktop.

## Overview of the Active Desktop Interface

-   [Accessing the Active Desktop](#accessing-the-active-desktop)
-   [Adding a Desktop Item](#adding-a-desktop-item)
-   [Enumerating the Desktop Items](#enumerating-the-desktop-items)

The Active Desktop is a feature introduced with Microsoft Internet Explorer 4.0 that enables you to include HTML documents and items (such as Microsoft ActiveX Controls and Java applets) directly to your desktop. The [**IActiveDesktop**](https://msdn.microsoft.com/en-us/library/Bb776357(v=VS.85).aspx) interface, which is part of the Windows Shell API, is used to programmatically add, remove, and modify the items on the desktop. Active Desktop items can also be added using a Channel Definition Format (CDF) file.

### Accessing the Active Desktop

To access the Active Desktop, a client application would need to create an instance of the ActiveDesktop object (CLSID\_ActiveDesktop) with the [CoCreateInstance](http://msdn.microsoft.com/library/ms686615(VS.85).aspx) function and retrieve a pointer to the object's [**IActiveDesktop**](https://msdn.microsoft.com/en-us/library/Bb776357(v=VS.85).aspx) interface.

The following sample shows how to retrieve a pointer to the [**IActiveDesktop**](https://msdn.microsoft.com/en-us/library/Bb776357(v=VS.85).aspx) interface.


```
HRESULT hr;
IActiveDesktop *pActiveDesktop;

//Create an instance of the Active Desktop
hr = CoCreateInstance(CLSID_ActiveDesktop, NULL, CLSCTX_INPROC_SERVER,
                      IID_IActiveDesktop, (void**)&pActiveDesktop);

//Insert code to call the IActiveDesktop methods

// Call the Release method
pActiveDesktop->Release();
```



### Adding a Desktop Item

There are three methods you can use to add a desktop item: [**IActiveDesktop::AddDesktopItem**](https://msdn.microsoft.com/en-us/library/Bb776343(v=VS.85).aspx), [**IActiveDesktop::AddDesktopItemWithUI**](https://msdn.microsoft.com/en-us/library/Bb776344(v=VS.85).aspx), and [**IActiveDesktop::AddUrl**](https://msdn.microsoft.com/en-us/library/Bb776345(v=VS.85).aspx). Each desktop item added to the Active Desktop must have a different source URL.

The [**IActiveDesktop::AddDesktopItemWithUI**](https://msdn.microsoft.com/en-us/library/Bb776344(v=VS.85).aspx) and [**IActiveDesktop::AddUrl**](https://msdn.microsoft.com/en-us/library/Bb776345(v=VS.85).aspx) methods both provide the option to display the various user interfaces that can be displayed before adding a desktop item to the Active Desktop. The interfaces verify whether users want to add the desktop item to their Active Desktop. The interfaces also notify users of any security risks that are warranted by the URL security zone settings, and they ask users if they would like to create a subscription for this desktop item. Both methods also provide a way of suppressing the user interfaces. The [**IActiveDesktop::AddDesktopItem**](https://msdn.microsoft.com/en-us/library/Bb776343(v=VS.85).aspx) method requires a call to [**IActiveDesktop::ApplyChanges**](https://msdn.microsoft.com/en-us/library/Bb776346(v=VS.85).aspx) in order to update the registry. For the **IActiveDesktop::AddDesktopItemWithUI**, the client application must immediately release the [**IActiveDesktop**](https://msdn.microsoft.com/en-us/library/Bb776357(v=VS.85).aspx) interface and then use the [CoCreateInstance](http://msdn.microsoft.com/library/ms686615(VS.85).aspx) function to retrieve an interface to an instance of the **ActiveDesktop** object that includes the newly added desktop item.

The [**IActiveDesktop::AddDesktopItem**](https://msdn.microsoft.com/en-us/library/Bb776343(v=VS.85).aspx) method adds the specified desktop item to the Active Desktop without any user interface, unless the URL security zone settings prevent it. If the URL security zone settings do not allow the desktop item to be added without prompting the user, the method fails. **IActiveDesktop::AddDesktopItem** also requires a call to [**IActiveDesktop::ApplyChanges**](https://msdn.microsoft.com/en-us/library/Bb776346(v=VS.85).aspx) in order to update the registry.

The following sample demonstrates how to add a desktop item with the [**IActiveDesktop::AddDesktopItem**](https://msdn.microsoft.com/en-us/library/Bb776343(v=VS.85).aspx) method.


```
HRESULT hr;
IActiveDesktop *pActiveDesktop;
COMPONENT compDesktopItem;

//Create an instance of the Active Desktop
hr = CoCreateInstance(CLSID_ActiveDesktop, NULL, CLSCTX_INPROC_SERVER,
                      IID_IActiveDesktop, (void**)&pActiveDesktop);

// Initialize the COMPONENT structure
compDesktopItem.dwSize = sizeof(COMPONENT);

// Insert code that adds the information about the desktop item 
// to the COMPONENT structure

// Add the desktop item
pActiveDesktop->AddDesktopItem(&compDesktopItem,0);

// Save the changes to the registry
pActiveDesktop->ApplyChanges(AD_APPLY_ALL);
```



### Enumerating the Desktop Items

To enumerate the desktop items currently installed on the Active Desktop, the client application needs to retrieve the total number of desktop items installed using the [**IActiveDesktop::GetDesktopItemCount**](https://msdn.microsoft.com/en-us/library/Bb776352(v=VS.85).aspx) method and then creating a loop that retrieves the [**COMPONENT**](https://msdn.microsoft.com/library/windows/desktop/bb773225) structure for each desktop item by calling the [**IActiveDesktop::GetDesktopItem**](https://msdn.microsoft.com/en-us/library/Bb776349(v=VS.85).aspx) method using the desktop item index.

The following sample demonstrates one way to enumerate the desktop items.


```
HRESULT hr;
IActiveDesktop *pActiveDesktop;
COMPONENT compDesktopItem;
int intCount;
int intIndex = 0;

//Create an instance of the Active Desktop
hr = CoCreateInstance(CLSID_ActiveDesktop, NULL, CLSCTX_INPROC_SERVER,
                      IID_IActiveDesktop, (void**)&pActiveDesktop);

pActiveDesktop->GetDesktopItemCount(&intCount,0);

compDesktopItem.dwSize = sizeof(COMPONENT);

while(intIndex<=(intCount-1))
{
    //get the COMPONENT structure for the current desktop item
    pActiveDesktop->GetDesktopItem(intIndex, &compDesktopItem,0);

    //Insert code that processes the structure

    //Increment the index
    intIndex++;

    //Insert code to clean-up structure for next component
}

// Call the Release method
pActiveDesktop->Release();
```



 

 




