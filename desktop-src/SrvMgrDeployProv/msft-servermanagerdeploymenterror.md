---
Description: Represents an error that happened during a deployment requests.
audience: developer
ms.assetid: 2f142b36-9044-4395-9887-3e9aa4d296bf
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_ServerManagerDeploymentError class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_ServerManagerDeploymentError class

Represents an error that happened during a deployment requests.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("deploymentprovider")]
class MSFT_ServerManagerDeploymentError
{
  String ErrorMessage;
  String ErrorId;
  uint8  ErrorCategory;
};
```

## Members

The **MSFT\_ServerManagerDeploymentError** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ServerManagerDeploymentError** class has these properties.

<dl> <dt>

**ErrorCategory**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the category of the error.

<dt>

<span id="NotSpecified"></span><span id="notspecified"></span><span id="NOTSPECIFIED"></span>

**NotSpecified** (0)


</dt> <dd></dd> <dt>

<span id="OpenError"></span><span id="openerror"></span><span id="OPENERROR"></span>

**OpenError** (1)


</dt> <dd></dd> <dt>

<span id="CloseError"></span><span id="closeerror"></span><span id="CLOSEERROR"></span>

**CloseError** (2)


</dt> <dd></dd> <dt>

<span id="DeviceError"></span><span id="deviceerror"></span><span id="DEVICEERROR"></span>

**DeviceError** (3)


</dt> <dd></dd> <dt>

<span id="DeadlockDetected"></span><span id="deadlockdetected"></span><span id="DEADLOCKDETECTED"></span>

**DeadlockDetected** (4)


</dt> <dd></dd> <dt>

<span id="InvalidArgument"></span><span id="invalidargument"></span><span id="INVALIDARGUMENT"></span>

**InvalidArgument** (5)


</dt> <dd></dd> <dt>

<span id="InvalidData"></span><span id="invaliddata"></span><span id="INVALIDDATA"></span>

**InvalidData** (6)


</dt> <dd></dd> <dt>

<span id="InvalidOperation"></span><span id="invalidoperation"></span><span id="INVALIDOPERATION"></span>

**InvalidOperation** (7)


</dt> <dd></dd> <dt>

<span id="InvalidResult"></span><span id="invalidresult"></span><span id="INVALIDRESULT"></span>

**InvalidResult** (8)


</dt> <dd></dd> <dt>

<span id="InvalidType"></span><span id="invalidtype"></span><span id="INVALIDTYPE"></span>

**InvalidType** (9)


</dt> <dd></dd> <dt>

<span id="MetadataError"></span><span id="metadataerror"></span><span id="METADATAERROR"></span>

**MetadataError** (10)


</dt> <dd></dd> <dt>

<span id="NotImplemented"></span><span id="notimplemented"></span><span id="NOTIMPLEMENTED"></span>

**NotImplemented** (11)


</dt> <dd></dd> <dt>

<span id="NotInstalled"></span><span id="notinstalled"></span><span id="NOTINSTALLED"></span>

**NotInstalled** (12)


</dt> <dd></dd> <dt>

<span id="ObjectNotFound"></span><span id="objectnotfound"></span><span id="OBJECTNOTFOUND"></span>

**ObjectNotFound** (13)


</dt> <dd></dd> <dt>

<span id="OperationStopped"></span><span id="operationstopped"></span><span id="OPERATIONSTOPPED"></span>

**OperationStopped** (14)


</dt> <dd></dd> <dt>

<span id="OperationTimeout"></span><span id="operationtimeout"></span><span id="OPERATIONTIMEOUT"></span>

**OperationTimeout** (15)


</dt> <dd></dd> <dt>

<span id="SyntaxError"></span><span id="syntaxerror"></span><span id="SYNTAXERROR"></span>

**SyntaxError** (16)


</dt> <dd></dd> <dt>

<span id="ParserError"></span><span id="parsererror"></span><span id="PARSERERROR"></span>

**ParserError** (17)


</dt> <dd></dd> <dt>

<span id="PermissionDenied"></span><span id="permissiondenied"></span><span id="PERMISSIONDENIED"></span>

**PermissionDenied** (18)


</dt> <dd></dd> <dt>

<span id="ResourceBusy"></span><span id="resourcebusy"></span><span id="RESOURCEBUSY"></span>

**ResourceBusy** (19)


</dt> <dd></dd> <dt>

<span id="ResourceExists"></span><span id="resourceexists"></span><span id="RESOURCEEXISTS"></span>

**ResourceExists** (20)


</dt> <dd></dd> <dt>

<span id="ResourceUnavailable"></span><span id="resourceunavailable"></span><span id="RESOURCEUNAVAILABLE"></span>

**ResourceUnavailable** (21)


</dt> <dd></dd> <dt>

<span id="ReadError"></span><span id="readerror"></span><span id="READERROR"></span>

**ReadError** (22)


</dt> <dd></dd> <dt>

<span id="WriteError"></span><span id="writeerror"></span><span id="WRITEERROR"></span>

**WriteError** (23)


</dt> <dd></dd> <dt>

<span id="FromStdErr"></span><span id="fromstderr"></span><span id="FROMSTDERR"></span>

**FromStdErr** (24)


</dt> <dd></dd> <dt>

<span id="FromStdErr"></span><span id="fromstderr"></span><span id="FROMSTDERR"></span>

**FromStdErr** (25)


</dt> <dd></dd> </dl>

</dd> <dt>

**ErrorId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the ID of the error.

</dd> <dt>

**ErrorMessage**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a description of the error.

</dd> </dl>

## Requirements



|                                     |                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                                  |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                                  |
| MOF<br/>                      | <dl> <dt>ServerManager.DeploymentProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ServerManager.DeploymentProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[ServerManager Deploymentprovider Provider Classes](server-manager-deployment.md)
</dt> </dl>

 

 




