---
title: VMRCAuthenticationType enumeration
description: The VMRCAuthenticationType enumeration specifies how the client is authenticated.
ms.assetid: '45c0c23b-521a-46bc-bf39-18ebf85b2e7c'
keywords: ["VMRCAuthenticationType enumeration Virtual Server"]
topic_type:
- apiref
api_name:
- VMRCAuthenticationType
api_location:
- VsComInterfaces.h
api_type:
- HeaderDef
---

# VMRCAuthenticationType enumeration

The **VMRCAuthenticationType** enumeration specifies how the client is authenticated.

## Syntax


```C++
typedef enum  { 
  vmVMRCAuthentication_Invalid    = -1,
  vmVMRCAuthentication_VNC        = 0,
  vmVMRCAuthentication_SRP        = 1,
  vmVMRCAuthentication_NTLM       = 2,
  vmVMRCAuthentication_Kerberos   = 3,
  vmVMRCAuthentication_Automatic  = 4
} VMRCAuthenticationType;
```



## Constants

<dl> <dt>

<span id="vmVMRCAuthentication_Invalid"></span><span id="vmvmrcauthentication_invalid"></span><span id="VMVMRCAUTHENTICATION_INVALID"></span>**vmVMRCAuthentication\_Invalid**
</dt> <dd>

Invalid authentication type.

</dd> <dt>

<span id="vmVMRCAuthentication_VNC"></span><span id="vmvmrcauthentication_vnc"></span><span id="VMVMRCAUTHENTICATION_VNC"></span>**vmVMRCAuthentication\_VNC**
</dt> <dd>

Allow client with no password or shared password.

When this authentication method is used, traditional VNC authentication is performed. If no password is specified, any client may connect to and control the virtual machine. If a password is specified, only those clients that know the password can connect to and control the virtual machine.

> [!Note]  
> This authentication method is not supported by Virtual Server.

 

</dd> <dt>

<span id="vmVMRCAuthentication_SRP"></span><span id="vmvmrcauthentication_srp"></span><span id="VMVMRCAUTHENTICATION_SRP"></span>**vmVMRCAuthentication\_SRP**
</dt> <dd>

Authenticate client using the Secure Remote Password (SRP) protocol as specified in RFC 2945.

> [!Note]  
> This authentication method is not supported by Virtual Server.

 

</dd> <dt>

<span id="vmVMRCAuthentication_NTLM"></span><span id="vmvmrcauthentication_ntlm"></span><span id="VMVMRCAUTHENTICATION_NTLM"></span>**vmVMRCAuthentication\_NTLM**
</dt> <dd>

Authenticate client using NTLM.

This method allows all Windows users with Administrative access to the computer to control the virtual machine.

</dd> <dt>

<span id="vmVMRCAuthentication_Kerberos"></span><span id="vmvmrcauthentication_kerberos"></span><span id="VMVMRCAUTHENTICATION_KERBEROS"></span>**vmVMRCAuthentication\_Kerberos**
</dt> <dd>

Authenticate client using the Kerberos protocol.

When used in conjunction with an Active Directory Domain Controller, this method allows Windows 2000 and Windows XP users with Administrative access to the computer to control the virtual machine.

</dd> <dt>

<span id="vmVMRCAuthentication_Automatic"></span><span id="vmvmrcauthentication_automatic"></span><span id="VMVMRCAUTHENTICATION_AUTOMATIC"></span>**vmVMRCAuthentication\_Automatic**
</dt> <dd>

Automatically choose between NTLM and Kerberos authentication.

When this authentication method is used, either Kerberos or NTLM authentication is used. The authentication protocol is negotiated by the client. This allows all Windows users with Administrative access to the computer to control the virtual machine.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





