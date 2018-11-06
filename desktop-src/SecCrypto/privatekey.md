---
Description: Represents the private key associated with a certificate.
ms.assetid: '26ad1d1c-17c5-4191-ac97-b911e62b4119'
title: PrivateKey object
ms.topic: interface
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- PrivateKey
api_type:
- COM
api_location:
- Capicom.dll
---

# PrivateKey object

\[The **PrivateKey** object is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Certificate2.PrivateKey Property**](https://msdn.microsoft.com/library/ms148460(v=VS.100).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

The **PrivateKey** object represents the [*private key*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) associated with a certificate.

## When to use

The **PrivateKey** object is used to perform the following tasks:

-   Retrieve information about the private key.
-   Open the private key container.
-   Delete the private key.

## Members

The **PrivateKey** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **PrivateKey** object has these methods.



| Method                                                  | Description                                                                                                                                                          |
|:--------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Delete**](privatekey-delete.md)                     | Deletes the private key container referenced by the **PrivateKey** object.<br/>                                                                                |
| [**IsAccessible**](privatekey-isaccessible.md)         | Retrieves a Boolean value that indicates whether the private key is accessible by the user. If true, the user can access the private key.<br/>                 |
| [**IsExportable**](privatekey-isexportable.md)         | Retrieves a Boolean value that indicates whether the private key can be exported. If true, the private key can be exported.<br/>                               |
| [**IsHardwareDevice**](privatekey-ishardwaredevice.md) | Retrieves a Boolean value that indicates whether the private key is stored on a hardware device. If true, the private key is stored on a hardware device.<br/> |
| [**IsMachineKeyset**](privatekey-ismachinekeyset.md)   | Retrieves a Boolean value that indicates whether the private key is a machine key. If true, the private key is a machine key.<br/>                             |
| [**IsProtected**](privatekey-isprotected.md)           | Retrieves a Boolean value that indicates whether the private key is protected. If true, the private key is protected.<br/>                                     |
| [**IsRemovable**](privatekey-isremovable.md)           | Retrieves a Boolean value that indicates whether the private key is on a removable device. If true, the private key is on a removable device.<br/>             |
| [**Open**](privatekey-open.md)                         | Accesses an existing key container.<br/>                                                                                                                       |



 

### Properties

The **PrivateKey** object has these properties.



| Property                                                                 | Access type          | Description                                                                                               |
|:-------------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------------------|
| [**ContainerName**](privatekey-containername.md)<br/>             | Read-only<br/> | Retrieves a string that contains the private key container name. This is the default property.<br/> |
| [**KeySpec**](privatekey-keyspec.md)<br/>                         | Read-only<br/> | Retrieves the key specification.<br/>                                                               |
| [**ProviderName**](privatekey-providername.md)<br/>               | Read-only<br/> | Retrieves a string that contains the name of the CSP.<br/>                                          |
| [**ProviderType**](privatekey-providertype.md)<br/>               | Read-only<br/> | Retrieves an enumeration value that specifies the type of provider.<br/>                            |
| [**UniqueContainerName**](privatekey-uniquecontainername.md)<br/> | Read-only<br/> | Retrieves a string that contains the unique private key container name.<br/>                        |



 

## Remarks

The **PrivateKey** object can be created, and it is safe for scripting. The ProgID for the **PrivateKey** object is CAPICOM.PrivateKey.1.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




