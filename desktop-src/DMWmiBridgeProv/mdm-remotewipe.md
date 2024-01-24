---
title: MDM_RemoteWipe class
description: The MDM\_RemoteWipe class allows a remote wipe of a device.
ms.assetid: 8c7c8705-8694-4ce3-ba21-ca610fe1f547
keywords:
- MDM_RemoteWipe class
- MDM_RemoteWipe class, described
topic_type:
- apiref
api_name:
- MDM_RemoteWipe
- MDM_RemoteWipe.InstanceID
- MDM_RemoteWipe.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_RemoteWipe class

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

The **MDM\_RemoteWipe** class allows a remote wipe of a device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv")]
class MDM_RemoteWipe
{
  string InstanceID;
  string ParentID;
};
```

## Members

The **MDM\_RemoteWipe** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MDM\_RemoteWipe** class has these methods.

| Method                                              | Description                                              |
|:----------------------------------------------------|:---------------------------------------------------------|
| [**doWipeMethod**](mdm-remotewipe-dowipemethod.md) | Triggers the device to start the remote wipe. |
| [**doWipePersistProvisionedDataMethod**](mdm-remotewipe-dowipepersistprovisioneddatamethod.md) | Triggers the device to back up provisioning data to a persistent location, and perform a remote wipe on the device. The information that was backed up will be restored and applied to the device when it resumes. |
| [**doWipePersistUserDataMethod**](mdm-remotewipe-dowipepersistuserdatamethod.md) | Triggers the device to start the remote wipe while persisting user accounts and data. |
| [**doWipeProtectedMethod**](mdm-remotewipe-dowipeprotectedmethod.md) | Triggers the device to start the remote wipe on the device, and fully clean the internal drive. In some device configurations, this command might leave the device unable to boot. |

### Properties

The **MDM\_RemoteWipe** class has these properties.

<dl> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Identifies the name of the parent node. For this class, the string is "RemoteWipe".

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/"

</dd> </dl>

## Example

The following example demonstrates how to use the RemoteWipe and invoke the doWipeMethod.

> [!Note]  
> This example must be executed under local system user. To do that, download the psexec tool from <https://technet.microsoft.com/sysinternals/bb897553.aspx> and run `psexec.exe -i -s cmd.exe` from an elevated admin command prompt.

``` syntax
$namespaceName = "root\cimv2\mdm\dmmap"
$className = "MDM_RemoteWipe"
$methodName = "doWipeMethod"

$session = New-CimSession

$params = New-Object Microsoft.Management.Infrastructure.CimMethodParametersCollection
$param = [Microsoft.Management.Infrastructure.CimMethodParameter]::Create("param", "", "String", "In")
$params.Add($param)

try
{
    $instance = Get-CimInstance -Namespace $namespaceName -ClassName $className -Filter "ParentID='./Vendor/MSFT' and InstanceID='RemoteWipe'"
    $session.InvokeMethod($namespaceName, $instance, $methodName, $params)
}
catch [Exception]
{
    write-host $_ | out-string
}
```

## Requirements

| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                                    |
| Minimum supported server | None supported                                                                      |
| Namespace                | Root\\CIMv2\\MDM\\DMMap                                                             |
| MOF                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |

## See also

<dl> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](/windows/client-management/mdm/using-powershell-scripting-with-the-wmi-bridge-provider)
</dt> </dl>
