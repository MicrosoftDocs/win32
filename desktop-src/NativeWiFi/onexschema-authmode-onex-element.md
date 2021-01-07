---
description: Specifies the type of credentials used for authentication.
ms.assetid: a56ce888-ec07-4ce8-a540-6d1890cb338d
title: authMode (OneX) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- authMode
api_type: 
- Schema
api_location: 
---

# authMode (OneX) Element

The authMode (OneX) element specifies the type of credentials used for authentication. The following table describes the possible values.



| Value         | Description                                                                                                                                                             |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| machineOrUser | Use machine or user credentials. When a user is logged on, the user's credentials are used for authentication. When no user is logged on, machine credentials are used. |
| machine       | Use machine credentials only.                                                                                                                                           |
| user          | Use user credentials only.                                                                                                                                              |
| guest         | Use guest (empty) credentials only.                                                                                                                                     |



 

This element is optional. When authMode is not specified in a profile, a value of `machineOrUser` is used.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

``` syntax
<xs:element name="authMode">
    <xs:simpleType>
        <xs:restriction
            base="string"
        >
            <xs:enumeration
                value="machineOrUser"
             />
            <xs:enumeration
                value="machine"
             />
            <xs:enumeration
                value="user"
             />
            <xs:enumeration
                value="guest"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The **authMode** element is defined by the [**OneX**](onexschema-onex-element.md) element.

## Remarks

This parameter can be set at the command line using the **netsh wlan set profileparameter** command. For more information, see [Netsh Commands for Wireless Local Area Network (wlan)](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc755301(v=ws.10)).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**OneX**](onexschema-onex-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**OneX**](onexschema-onex-element.md)
</dt> </dl>

 

 
