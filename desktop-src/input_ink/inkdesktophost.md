---
Description: Implements the IInkDesktopHost interface.
ms.assetid: 7a577536-405b-400d-89bc-c3b3894b448d
title: InkDesktopHost class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkDesktopHost
api_type: 
- COM
api_location: 
- InkPresenterDesktop.idl
---

# InkDesktopHost class

Implements the [**IInkDesktopHost**](https://msdn.microsoft.com/en-us/library/Mt622149(v=VS.85).aspx) interface.

An [**IInkDesktopHost**](https://msdn.microsoft.com/en-us/library/Mt622149(v=VS.85).aspx) object enables ink input, processing, and rendering through the creation of an app thread to host an [**IInkPresenterDesktop**](https://msdn.microsoft.com/en-us/library/Mt622155(v=VS.85).aspx) object and insert it into the app's [DirectComposition](https://msdn.microsoft.com/en-us/library/Hh437371(v=VS.85).aspx) visual tree.

## Members

The **InkDesktopHost** class inherits from the [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) interface. **InkDesktopHost** also has these types of members:

-   [Methods](#methods)

### Methods

The **InkDesktopHost** class has these methods.



| Method                                                                                    | Description                                                                                                                                                                                                                                                 |
|:------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateAndInitializeInkPresenter**](inkdesktophost-createandinitializeinkpresenter.md) | Creates an [**IInkPresenterDesktop**](https://msdn.microsoft.com/en-us/library/Mt622155(v=VS.85).aspx) object on an application thread, connects it to the app's [DirectComposition](https://msdn.microsoft.com/en-us/library/Hh437371(v=VS.85).aspx) visual tree, and sets the size of the object.<br/> |
| [**CreateInkPresenter**](inkdesktophost-createinkpresenter.md)                           | Creates an [**IInkPresenterDesktop**](https://msdn.microsoft.com/en-us/library/Mt622155(v=VS.85).aspx) object on an application thread.<br/>                                                                                                                                 |
| [**QueueWorkItem**](inkdesktophost-queueworkitem.md)                                     | Add an ink operation to a work queue for execution on the **InkDesktopHost** thread.<br/>                                                                                                                                                             |



 

## Creation\\Access Functions

Use the following to retrieve a reference to the object:



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>[<strong>CoCreateInstance</strong>](https://msdn.microsoft.com/en-us/library/ms686615(v=VS.85).aspx)</td>
<td>Call [<strong>CoCreateInstance</strong>](https://msdn.microsoft.com/en-us/library/ms686615(v=VS.85).aspx) with the class identifier <strong>InkDesktopHost</strong>.<br/> <span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>CoCreateInstance(__uuidof(InkDesktopHost), 
  nullptr, 
  CLSCTX_INPROC_SERVER, 
  IID_PPV_ARGS(&amp;_spInkHost));</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                        |
| Minimum supported server<br/> | None supported<br/>                                                                          |
| Header<br/>                   | <dl> <dt>InkPresenterDesktop.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>InkPresenterDesktop.idl</dt> </dl> |
| IID<br/>                      | IID\_IInkDesktopHost is defined as 4ce7d875-a981-4140-a1ff-ad93258e8d59<br/>                 |



## See also

<dl> <dt>

[Ink presenter classes](ink-presenter-classes.md)
</dt> <dt>

[Pen and stylus interactions](https://msdn.microsoft.com/en-us/library/Mt187311(v=WIN.10).aspx)
</dt> <dt>

**Samples**
</dt> <dt>

[Ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620308)
</dt> <dt>

[Simple ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620312)
</dt> <dt>

[Complex ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620314)
</dt> </dl>

 

 




