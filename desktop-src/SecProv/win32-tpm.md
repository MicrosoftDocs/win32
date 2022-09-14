---
description: Represents the Trusted Platform Module (TPM), a hardware security chip that provides a root of trust for a computer system.
ms.assetid: 'da4ba366-49af-420e-a2ad-80bba34b3b00'
title: Win32_Tpm class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm
- Win32_Tpm.IsActivated_InitialValue
- Win32_Tpm.IsEnabled_InitialValue
- Win32_Tpm.IsOwned_InitialValue
- Win32_Tpm.SpecVersion
- Win32_Tpm.ManufacturerVersion
- Win32_Tpm.ManufacturerVersionInfo
- Win32_Tpm.ManufacturerId
- Win32_Tpm.PhysicalPresenceVersionInfo
api_type: 
- DllExport
api_location: 
- Win32_tpm.dll
---

# Win32\_Tpm class

The **Win32\_Tpm** class represents the Trusted Platform Module (TPM), a hardware security chip that provides a root of trust for a computer system.

## Syntax

``` syntax
class Win32_Tpm
{
  boolean IsActivated_InitialValue;
  boolean IsEnabled_InitialValue;
  boolean IsOwned_InitialValue;
  string  SpecVersion;
  string  ManufacturerVersion;
  string  ManufacturerVersionInfo;
  uint32  ManufacturerId;
  string  PhysicalPresenceVersionInfo;
};
```

## Members

The **Win32\_Tpm** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_Tpm** class has these methods.



| Method                                                                                   | Description                                                                                                                                                                                 |
|:-----------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddBlockedCommand**](addblockedcommand-win32-tpm.md)                                 | Adds a TPM command to the local list of commands blocked on Windows.<br/>                                                                                                             |
| [**ChangeOwnerAuth**](changeownerauth-win32-tpm.md)                                     | Changes the TPM owner authorization value.<br/>                                                                                                                                       |
| [**Clear**](clear-win32-tpm.md)                                                         | Resets the TPM to its factory-default state.<br/>                                                                                                                                     |
| [**ConvertToOwnerAuth**](converttoownerauth-win32-tpm.md)                               | Converts a user-provided passphrase to a 20-byte owner authorization value that can be used to interact with the TPM.<br/>                                                            |
| [**CreateEndorsementKeyPair**](createendorsementkeypair-win32-tpm.md)                   | Creates a 2048-bit endorsement key pair on the TPM.<br/>                                                                                                                              |
| [**Disable**](disable-win32-tpm.md)                                                     | Allows the TPM owner to disable the TPM.<br/>                                                                                                                                         |
| [**Enable**](enable-win32-tpm.md)                                                       | Allows the TPM owner to enable the TPM.<br/>                                                                                                                                          |
| [**GetPhysicalPresenceRequest**](getphysicalpresencerequest-win32-tpm.md)               | Gets and returns the pending TPM physical presence operation. Use the [**SetPhysicalPresenceRequest**](setphysicalpresencerequest-win32-tpm.md) method to request an operation.<br/> |
| [**GetPhysicalPresenceResponse**](getphysicalpresenceresponse-win32-tpm.md)             | Gets and returns the results from a TPM physical presence operation that was performed.<br/>                                                                                          |
| [**GetPhysicalPresenceTransition**](getphysicalpresencetransition-win32-tpm.md)         | Indicates the user action that is needed to perform a TPM physical presence operation.<br/>                                                                                           |
| [**IsActivated**](isactivated-win32-tpm.md)                                             | Indicates whether the TPM is activated.<br/>                                                                                                                                          |
| [**IsCommandBlocked**](iscommandblocked-win32-tpm.md)                                   | Indicates whether the TPM command can run on this operating system.<br/>                                                                                                              |
| [**IsCommandPresent**](iscommandpresent-win32-tpm.md)                                   | Indicates whether a TPM command is supported by this computer.<br/>                                                                                                                   |
| [**IsEnabled**](isenabled-win32-tpm.md)                                                 | Indicates whether the TPM is enabled.<br/>                                                                                                                                            |
| [**IsEndorsementKeyPairPresent**](isendorsementkeypairpresent-win32-tpm.md)             | Indicates whether the TPM has an endorsement key pair.<br/>                                                                                                                           |
| [**IsOwned**](isowned-win32-tpm.md)                                                     | Indicates whether the TPM has an owner.<br/>                                                                                                                                          |
| [**IsOwnerClearDisabled**](isownercleardisabled-win32-tpm.md)                           | Indicates whether the TPM owner can clear the TPM.<br/>                                                                                                                               |
| [**IsOwnershipAllowed**](isownershipallowed-win32-tpm.md)                               | Indicates whether a TPM owner can be installed.<br/>                                                                                                                                  |
| [**IsPhysicalClearDisabled**](isphysicalcleardisabled-win32-tpm.md)                     | Indicates whether a TPM physical presence operation can clear the TPM.<br/>                                                                                                           |
| [**IsPhysicalPresenceHardwareEnabled**](isphysicalpresencehardwareenabled-win32-tpm.md) | Indicates whether this computer supports a dedicated hardware path to signal physical presence.<br/>                                                                                  |
| [**IsSrkAuthCompatible**](issrkauthcompatible-win32-tpm.md)                             | Indicates whether the Storage Root Key (SRK) authorization is compatible with Windows.<br/>                                                                                           |
| [**RemoveBlockedCommand**](removeblockedcommand-win32-tpm.md)                           | Removes a TPM command from the local list of commands blocked by Windows.<br/>                                                                                                        |
| [**ResetAuthLockOut**](resetauthlockout-win32-tpm.md)                                   | Resets the time-out period or other mechanism that TPM manufacturers implement to protect against dictionary attacks on the TPM.<br/>                                                 |
| [**ResetSrkAuth**](resetsrkauth-win32-tpm.md)                                           | Resets the Storage Root Key (SRK) authorization value to be compatible with Windows.<br/>                                                                                             |
| [**SelfTest**](selftest-win32-tpm.md)                                                   | Performs a self-test of the TPM and returns the result.<br/>                                                                                                                          |
| [**SetPhysicalPresenceRequest**](setphysicalpresencerequest-win32-tpm.md)               | Requests a TPM physical presence operation to run.<br/>                                                                                                                               |
| [**TakeOwnership**](takeownership-win32-tpm.md)                                         | Installs an owner for the TPM.<br/>                                                                                                                                                   |



 

### Properties

The **Win32\_Tpm** class has these properties.

<dl> <dt>

**IsActivated\_InitialValue**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the TPM is activated.

**true** if the device is activated (that is, if **IsActivated\_InitialValue** is true); otherwise, **false**.

This value is stored when the class is instantiated. It is possible for the TPM to change state between the instantiation and when you check this value. To check whether the TPM is activated in real time, use the [**IsActivated**](isactivated-win32-tpm.md) method.

**Windows Server 2008 and Windows Vista:** This property is not available.

</dd> <dt>

**IsEnabled\_InitialValue**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the TPM is enabled.

**true** if the device is enabled (that is, if **IsEnabled\_InitialValue** is true); otherwise, **false**.

This value is stored when the class is instantiated. It is possible for the TPM to change state between the instantiation and when you check this value. To check whether the TPM is enabled in real time, use the [**IsEnabled**](isenabled-win32-tpm.md) method.

**Windows Server 2008 and Windows Vista:** This property is not available.

</dd> <dt>

**IsOwned\_InitialValue**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the TPM has an owner.

**true** if the device has an owner (that is, if **IsOwned\_InitialValue** is true); otherwise, **false**.

This value is stored when the class is instantiated. It is possible for the TPM to change state between the instantiation and when you check this value. To check whether the TPM is owned in real time, use the [**IsOwned**](isowned-win32-tpm.md) method.

**Windows Server 2008 and Windows Vista:** This property is not available.

</dd> <dt>

**ManufacturerId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The identifying information that uniquely names the TPM manufacturer.

When the data is unavailable, zero is returned.

This integer value can be translated to a string value by interpreting each byte as an ASCII character. For example, an integer value of 1414548736 can be divided into these 4 bytes: 0x54, 0x50, 0x4D, and 0x00. Assuming the string is interpreted from left to right, this integer value translated to a string value of "TPM".

</dd> <dt>

**ManufacturerVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of the TPM, as specified by the manufacturer.

When the data is unavailable, "Not Supported" is returned.

</dd> <dt>

**ManufacturerVersionInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Other manufacturer-specific version information for the TPM.

When the data is unavailable, "Not Supported" is returned.

</dd> <dt>

**PhysicalPresenceVersionInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of the Physical Presence Interface, a communication mechanism used to run device operations that require physical presence, that the computer supports.

This interface must be available to run TPM physical presence operations. The **Win32\_Tpm** methods [**SetPhysicalPresenceRequest**](setphysicalpresencerequest-win32-tpm.md), [**GetPhysicalPresenceRequest**](getphysicalpresencerequest-win32-tpm.md), [**GetPhysicalPresenceTransition**](getphysicalpresencetransition-win32-tpm.md), and [**GetPhysicalPresenceResponse**](getphysicalpresenceresponse-win32-tpm.md) expose the capabilities of the Physical Presence Interface.

When the data is unavailable, "Not Supported" is returned.

</dd> <dt>

**SpecVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of the Trusted Computing Group (TCG) specification that the TPM supports. This value includes the major and minor TCG specification version, the specification revision level, and the errata revision level. All values are in hexadecimal. For example, a version information of "1.2, 2, 0" indicates that the device was implemented to TCG specification version 1.2, revision level 2, and with no errata.

When the data is unavailable, "Not Supported" is returned.

</dd> </dl>

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftTpm<br/>                                            |
| MOF<br/>                      | <dl> <dt>Win32\_tpm.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Win32\_tpm.dll</dt> </dl> |



 

 
