---
title: View ListViewMode property
description: The ListViewMode property sets or returns the mode of the list view. This property is read/write.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c2880ebf-290b-4e8b-95be-5612601dfa8b'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["ListViewMode property MMC", "ListViewMode property MMC , View object", "View object MMC , ListViewMode property", "ListViewMode property MMC , View interface", "View interface MMC , ListViewMode property"]
topic_type:
- apiref
api_name:
- View.ListViewMode
- View.ListViewMode
api_location:
- Mmc.exe
api_type:
- COM
---

# View::ListViewMode property

The **ListViewMode** property sets or returns the mode of the list view. This property is read/write.

## Syntax


```VB
Property ListViewMode As ListViewMode
```



## Property value

The list view's mode, as one of the following [**ListViewMode**](listviewmode.md) enumerated types.

<dt>

<span id="ListMode_Small_Icons"></span><span id="listmode_small_icons"></span><span id="LISTMODE_SMALL_ICONS"></span>

<span id="ListMode_Small_Icons"></span><span id="listmode_small_icons"></span><span id="LISTMODE_SMALL_ICONS"></span>**ListMode\_Small\_Icons**


</dt> <dd>

The list view is displayed with small icons.

</dd> <dt>

<span id="ListMode_Large_Icons"></span><span id="listmode_large_icons"></span><span id="LISTMODE_LARGE_ICONS"></span>

<span id="ListMode_Large_Icons"></span><span id="listmode_large_icons"></span><span id="LISTMODE_LARGE_ICONS"></span>**ListMode\_Large\_Icons**


</dt> <dd>

The list view is displayed with large icons.

</dd> <dt>

<span id="ListMode_List"></span><span id="listmode_list"></span><span id="LISTMODE_LIST"></span>

<span id="ListMode_List"></span><span id="listmode_list"></span><span id="LISTMODE_LIST"></span>**ListMode\_List**


</dt> <dd>

A simple list view is displayed.

</dd> <dt>

<span id="ListMode_Detail"></span><span id="listmode_detail"></span><span id="LISTMODE_DETAIL"></span>

<span id="ListMode_Detail"></span><span id="listmode_detail"></span><span id="LISTMODE_DETAIL"></span>**ListMode\_Detail**


</dt> <dd>

A detailed list view is displayed.

</dd> <dt>

<span id="ListMode_Filtered"></span><span id="listmode_filtered"></span><span id="LISTMODE_FILTERED"></span>

<span id="ListMode_Filtered"></span><span id="listmode_filtered"></span><span id="LISTMODE_FILTERED"></span>**ListMode\_Filtered**


</dt> <dd>

A filtered list view is displayed.

</dd> </dl>

## Examples


```VB
Dim LVM As MMC20.ListViewMode
 
' Retrieve the View's ListViewMode property.
LVM = objView.ListViewMode
 
' Display a message that states the ListViewMode in effect.
Select Case LVM
  Case ListMode_Detail
      MsgBox ("List view is in Detail mode.")
  Case ListMode_Filtered
      MsgBox ("List view is in Filtered mode.")
  Case ListMode_Large_Icons
      MsgBox ("List view is in Large icon mode.")
  Case ListMode_List
      MsgBox ("List view is in Simple list mode.")
  Case ListMode_Small_Icons
      MsgBox ("List view is in Small icon mode.")
  Case Else
      MsgBox ("Unexpected value for ListViewMode")
End Select
 
' Set the View's ListView Mode property.
objView.ListViewMode = ListMode_Large_Icons
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_View is defined as 6EFC2DA2-B38C-457E-9ABB-ED2D189B8C38<br/>               |



## See also

<dl> <dt>

[**ListViewMode**](listviewmode.md)
</dt> </dl>

 

 





