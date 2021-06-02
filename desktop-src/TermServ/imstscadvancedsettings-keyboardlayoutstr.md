---
title: IMsTscAdvancedSettings KeyBoardLayoutStr property
description: Specifies the name of the active input locale identifier (formerly called the keyboard layout) to use for the connection.
ms.assetid: a469c602-84a8-44c6-9c0f-76262961b527
ms.tgt_platform: multiple
keywords:
- KeyBoardLayoutStr property Remote Desktop Services
- KeyBoardLayoutStr property Remote Desktop Services , IMsTscAdvancedSettings interface
- IMsTscAdvancedSettings interface Remote Desktop Services , KeyBoardLayoutStr property
topic_type:
- apiref
api_name:
- IMsTscAdvancedSettings.KeyBoardLayoutStr
- IMsTscAdvancedSettings.put_KeyBoardLayoutStr
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAdvancedSettings::KeyBoardLayoutStr property

Specifies the name of the active input locale identifier (formerly called the keyboard layout) to use for the connection.

If this property is not set, the control uses the default layout returned by the [**GetKeyboardLayout**](/windows/desktop/api/winuser/nf-winuser-getkeyboardlayout) function.

This property is write-only.

## Syntax


```C++
HRESULT put_KeyBoardLayoutStr(
  [in] BSTR KeyBoardLayoutStr
);
```



## Property value

The name of the active input locale identifier.

## Error codes

Returns **S\_OK** if successful.

## Remarks

The property is an eight digit hexadecimal number in string form. The lower four digits represent the language identifier, and the upper four digits represent the keyboard variation within that language. So, for example, "00000409" would represent the default US English keyboard because "0409" is the US English language identifier. The Dvorak variation of the US English keyboard has an identifier of "00010409". You can find the available keyboard layouts, listed by their keyboard layout identifiers, in the registry under

```
HKEY_LOCAL_MACHINE
   SYSTEM
      ControlSet001
         Control
            Keyboard Layouts
```

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                            |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>    |
| IID<br/>                      | IID\_IMsTscAdvancedSettings is defined as 809945cc-4b3b-4a92-a6b0-dbf9b5f2ef2d<br/> |



## See also

<dl> <dt>

[**IMsTscAdvancedSettings**](imstscadvancedsettings-interface.md)
</dt> </dl>

 

