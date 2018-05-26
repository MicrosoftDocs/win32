---
title: Views Add method
description: The Add method adds a view at a specified root node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 86c809b4-6533-4e02-a49e-f141fac228b1
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Add method MMC
- Add method MMC , Views object
- Views object MMC , Add method
- Add method MMC , Views interface
- Views interface MMC , Add method
topic_type:
- apiref
api_name:
- Views.Add
- Views.Add
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Views::Add method

The **Add** method adds a view at a specified root node.

## Syntax


```VB
Views.Add( _
  ByVal Node As Node, _
  ByVal ViewOptions As ViewOptions _
)
```



## Parameters

<dl> <dt>

*Node* 
</dt> <dd>

The node to serve as the root of the added view.

</dd> <dt>

*ViewOptions* 
</dt> <dd>

This parameter can be one or more of the following [**ViewOptions**](/windows/win32/MmcObj/ne-mmcobj-viewoptions?branch=master) enumeration types. These flags can be combined using a bitwise OR operation.

<dt>

<span id="ViewOption_Default"></span><span id="viewoption_default"></span><span id="VIEWOPTION_DEFAULT"></span>

<span id="ViewOption_Default"></span><span id="viewoption_default"></span><span id="VIEWOPTION_DEFAULT"></span>**ViewOption\_Default**


</dt> <dd>

The view is added with default settings.

</dd> <dt>

<span id="ViewOption_ScopeTreeHidden"></span><span id="viewoption_scopetreehidden"></span><span id="VIEWOPTION_SCOPETREEHIDDEN"></span>

<span id="ViewOption_ScopeTreeHidden"></span><span id="viewoption_scopetreehidden"></span><span id="VIEWOPTION_SCOPETREEHIDDEN"></span>**ViewOption\_ScopeTreeHidden**


</dt> <dd>

The view is added with the scope tree pane hidden. The user will not be able to show the scope tree, as the *Console Tree* check box will be disabled in the *Customize View* dialog.

</dd> <dt>

<span id="ViewOption_NoToolBars"></span><span id="viewoption_notoolbars"></span><span id="VIEWOPTION_NOTOOLBARS"></span>

<span id="ViewOption_NoToolBars"></span><span id="viewoption_notoolbars"></span><span id="VIEWOPTION_NOTOOLBARS"></span>**ViewOption\_NoToolBars**


</dt> <dd>

The view is added with toolbars hidden.

</dd> <dt>

<span id="ViewOption_NotPersistable"></span><span id="viewoption_notpersistable"></span><span id="VIEWOPTION_NOTPERSISTABLE"></span>

<span id="ViewOption_NotPersistable"></span><span id="viewoption_notpersistable"></span><span id="VIEWOPTION_NOTPERSISTABLE"></span>**ViewOption\_NotPersistable**


</dt> <dd>

The view is temporary (without persistence capability).

</dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Examples


```VB
' Add a new view.
' objRoot is a Node object, set to the Document's RootNode.
objViews.Add objRoot, _
         ViewOption_ScopeTreeHidden Or _
         ViewOption_NoToolBars
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Views is defined as D6B8C29D-A1FF-4D72-AAB0-E381E9B9338D<br/>              |



## See also

<dl> <dt>

[**ViewOptions**](/windows/win32/MmcObj/ne-mmcobj-viewoptions?branch=master)
</dt> <dt>

[**Views.Count**](views-count.md)
</dt> <dt>

[**Views.Item**](views-item.md)
</dt> </dl>

 

 





