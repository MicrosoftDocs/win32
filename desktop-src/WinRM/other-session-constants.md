---
title: Other Session Constants (WSManDisp.h)
description: Specify encoding, encryption, and service principal name port.
ms.assetid: a921b7bc-1f40-427c-971f-c0bc9c9f6887
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- WSManFlagUTF8
- WSManFlagNoEncryption
- WSManFlagEnableSPNServerPort
- WSManFlagUTF16
api_location:
- WSManDisp.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Other Session Constants

Constants, listed in the following list, in the **\_\_WSManSessionFlags** enumeration that specify encoding, encryption, and service principal name port.

<dl> <dt>

<span id="WSManFlagUTF8"></span><span id="wsmanflagutf8"></span><span id="WSMANFLAGUTF8"></span>**WSManFlagUTF8**
</dt> <dd> <dl> <dt>

1 (0x1)
</dt> <dt>



Sends the request in UTF8 rather than UTF16.

The associated scripting method is [**WSMan.SessionFlagUTF8**](wsman-sessionflagutf8.md) and the C++ method is [**IWSManEx.SessionFlagUTF8**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex-sessionflagutf8).


</dt> </dl> </dd> <dt>

<span id="WSManFlagNoEncryption"></span><span id="wsmanflagnoencryption"></span><span id="WSMANFLAGNOENCRYPTION"></span>**WSManFlagNoEncryption**
</dt> <dd> <dl> <dt>

1048576 (0x100000)
</dt> <dt>



Do not encrypt the messages sent over the network. This setting is allowed only if the [*listener*](windows-remote-management-glossary.md) is configured so that **AllowUnencrypted** is set to **True**.

The associated scripting method is [**WSMan.SessionFlagNoEncryption**](wsman-sessionflagnoencryption.md) and the C++ method is [**IWSManEx.SessionFlagNoEncryption**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex-sessionflagnoencryption).


</dt> </dl> </dd> <dt>

<span id="WSManFlagEnableSPNServerPort"></span><span id="wsmanflagenablespnserverport"></span><span id="WSMANFLAGENABLESPNSERVERPORT"></span>**WSManFlagEnableSPNServerPort**
</dt> <dd> <dl> <dt>

4194304 (0x400000)
</dt> <dt>



Specify the Service Principal Name (SPN) port when connecting directly to remote BMC hardware, also known as an [*out-of-band*](windows-remote-management-glossary.md) connection. Because both the WinRM server computer and the BMC hardware can share the same IP address, this flag indicates that the SPN port number must be used to determine whether the connection is to the service or directly to the BMC. For more information, see [Name Formats for Unique SPNs](/windows/desktop/AD/name-formats-for-unique-spns).

The associated scripting method is [**WSMan.SessionFlagEnableSPNServerPort**](wsman-sessionflagenablespnserverport.md) and the C++ method is [**IWSManEx.SessionFlagEnableSPNServerPort**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex-sessionflagenablespnserverport).


</dt> </dl> </dd> <dt>

<span id="WSManFlagUTF16"></span><span id="wsmanflagutf16"></span><span id="WSMANFLAGUTF16"></span>**WSManFlagUTF16**
</dt> <dd> <dl> <dt>

0x800000
</dt> <dt>



Sends the request in UTF16.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>WSManDisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WSManDisp.idl</dt> </dl> |



## See also

<dl> <dt>

[Session Constants](session-constants.md)
</dt> </dl>

 

