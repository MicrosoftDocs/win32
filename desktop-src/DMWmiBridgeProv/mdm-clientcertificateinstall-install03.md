---
title: MDM_ClientCertificateInstall_Install03 class
description: The MDM\_ClientCertificateInstall\_Install03 class enables the enterprise to set the installation of client certificates.
ms.assetid: 0083e54c-e621-47da-a20d-17c8bbf7dd3a
keywords:
- MDM_ClientCertificateInstall_Install03 class
- MDM_ClientCertificateInstall_Install03 class, described
topic_type:
- apiref
api_name:
- MDM_ClientCertificateInstall_Install03
- MDM_ClientCertificateInstall_Install03.InstanceID
- MDM_ClientCertificateInstall_Install03.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_ClientCertificateInstall\_Install03 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_ClientCertificateInstall\_Install03** class enables the enterprise to set the installation of client certificates.Required for SCEP certificate enrollment. Parent node to group SCEP cert install related request.

> [!Note]  
> Even though the child nodes under Install support Replace commands, after the Exec command is sent to the device, the device will take the values which are set when the Exec command is accepted. The server should not expect the node value change after Exec command is accepted will impact the current undergoing enrollment. The server should check the Status node value and make sure the device is not at unknown stage before changing child node values.

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[InPartition("local-system", "local-user"), dynamic, provider("DMWmiBridgeProv")]
class MDM_ClientCertificateInstall_Install03
{
  string InstanceID;
  string ParentID;
  string ServerURL;
  string Challenge;
  string EKUMapping;
  sint32 KeyUsage;
  string SubjectName;
  sint32 KeyProtection;
  sint32 RetryDelay;
  sint32 RetryCount;
  string TemplateName;
  sint32 KeyLength;
  string HashAlgorithm;
  string CAThumbprint;
  string SubjectAlternativeNames;
  string ValidPeriod;
  sint32 ValidPeriodUnits;
  string ContainerName;
  string CustomTextToShowInPrompt;
  string AADKeyIdentifierList;
};
```

## Members

The **MDM\_ClientCertificateInstall\_Install03** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MDM\_ClientCertificateInstall\_Install03** class has these methods.



| Method                                                                      | Description                                                                   |
|:----------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| [**EnrollMethod**](mdm-clientcertificateinstall-install03-enrollmethod.md) | Required. Triggers the device to start the certificate enrollment.<br/> |



 

### Properties

The **MDM\_ClientCertificateInstall\_Install03** class has these properties.

<dl> <dt>

[AADKeyIdentifierList](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-aadkeyidentifierlist)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[CAThumbprint](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-cathumbprint)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[Challenge](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-challenge)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[ContainerName](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-pfxcertinstall-uniqueid-containername)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[CustomTextToShowInPrompt](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-customtexttoshowinprompt)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[EKUMapping](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-ekumapping)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HashAlgorithm](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-hashalgorithm)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Required for SCEP certificate enrollment. Parent node to group SCEP cert install related request.

The Format is node.

</dd> <dt>

[KeyLength](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-keylength)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[KeyProtection](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-keyprotection)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[KeyUsage](/windows/client-management/mdm/clientcertificateinstall-csp)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Describes the full path to the parent node.

The string is "./Vendor/MSFT/ClientCertificateInstall/PFXCertInstall/SCEP/*UniqueID*"

</dd> <dt>

[RetryCount](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-retrycount)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[RetryDelay](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-retrydelay)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[ServerURL](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-serverurl)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[SubjectAlternativeNames](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-subjectalternativenames)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[SubjectName](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-subjectname)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[TemplateName](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-templatename)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[ValidPeriod](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-validperiod)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[ValidPeriodUnits](/windows/client-management/mdm/clientcertificateinstall-csp#clientcertificateinstall-scep-uniqueid-install-validperiodunits)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](/windows/client-management/mdm/using-powershell-scripting-with-the-wmi-bridge-provider)
</dt> </dl>

 

