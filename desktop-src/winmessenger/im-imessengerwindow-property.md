---
title: IMessengerWindow Property property
description: Sets or retrieves the conversation window properties.
ms.assetid: '64177894-990c-4ff0-9a90-a6cbc907d326'
keywords: ["Property property Windows Messenger", "Property property Windows Messenger , IMessengerWindow interface", "IMessengerWindow interface Windows Messenger , Property property"]
topic_type:
- apiref
api_name:
- IMessengerWindow.Property
- IMessengerWindow.get_Property
- IMessengerWindow.put_Property
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerWindow::Property property

\[**Property** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Sets or retrieves the conversation window properties.

This property is read/write.

## Syntax


```C++
HRESULT put_Property(
  [in]          MWINDOWPROPERTY ePropType,
  [in]          VARIANT         vPropVal
);

HRESULT get_Property(
  [in]          MWINDOWPROPERTY ePropType,
  [out, retval] VARIANT         *pvPropVal
);
```



## Property value

A pointer to a **VARIANT** that contains the property value. (Variant type differs depending on the property being set or retrieved.)

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                                                                 |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | The property value has been set successfully. <br/>                               |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pvPropVal* is a **NULL** pointer.<br/>                                           |
| <dl> <dt>E\_INVALIDARG</dt> </dl>              | *ePropType* is out of range.<br/>                                                 |
| <dl> <dt>S\_FALSE</dt> </dl>                   | The method was used twice with the same values. <br/>                             |
| <dl> <dt>E\_NOTIMPL</dt> </dl>                 | Attempted to use the method on the Phone window or main application window. <br/> |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                                                     |
|------------|-----------------------------------------------------------------------------|
| 0x80004001 | Attempted to use the method on the Phone window or main application window. |
| 0x80070057 | *ePropType* is out of range.                                                |



 

> [!Note]  
> The **get\_Property** property is available for scripting languages; **put\_Property** is not.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger 
Public MsgrWindow As MessengerAPI.IMessengerWindow 
Public MsgrContact As MessengerAPI.IMessengerContact

Private Sub GetWindowProperty_Click() 
    On Error Resume Next 
    FormContactName.Show vbModal 'Open dialog for user input 
    Dim PropSB, PropTB As Variant 
    If bDialogCancel = False Then 
        If bContactasObject = True Then 
            Set MsgrContact = Nothing 
            Set MsgrContact = MsgrUIA.GetContact(strContactName, strServiceID) 
            MsgrWindow = MsgrUIA.InstantMessage(MsgrContact) 
            ' Get the SideBar Status 
            PropSB = MsgrWindow.Property(MWINDOWPROP_VIEW_SIDEBAR) 
            ' Get the ToolBar Status 
            PropTB = MsgrWindow.Property(MWINDOWPROP_VIEW_TOOLBAR) 
        End If 
    End If 
    bContactasObject = False 
    ErrorTrap ("IMessengerWindow.Property") 'Error handling routine 
End Sub
```



## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





