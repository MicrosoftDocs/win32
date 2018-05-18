---
Description: 'Not supported. Use the SoftwareLicensingProduct class.'
ms.assetid: '166f8d04-90ec-4dae-80fc-64d1a5216dcf'
title: SoftwareLicensingProduct class
---

# SoftwareLicensingProduct class

Not supported. Use the [**SoftwareLicensingProduct**](https://msdn.microsoft.com/library/cc534596) class.

**Windows Vista and Windows Server 2008:** This class exposes the product-specific properties and methods of the Software Licensing service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class SoftwareLicensingProduct
{
  string   ID;
  string   Name;
  string   Description;
  string   ApplicationID;
  string   ProcessorURL;
  string   MachineURL;
  string   ProductKeyURL;
  string   UseLicenseURL;
  uint32   LicenseStatus;
  uint32   LicenseStatusReason;
  uint32   GracePeriodRemaining;
  datetime EvaluationEndDate;
  string   OfflineInstallationId;
  string   PartialProductKey;
  string   ProductKeyID;
  string   LicenseFamily;
  string   LicenseDependsOn;
  boolean  LicenseIsAddon;
};
```

## Members

The **SoftwareLicensingProduct** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SoftwareLicensingProduct** class has these methods.



| Method                                                                                              | Description                                                                                                                                |
|:----------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| [**Activate**](activate-softwarelicensingproduct-vista.md)                                         | Activates the product. <br/>                                                                                                         |
| [**DepositOfflineConfirmationId**](depositofflineconfirmationid-softwarelicensingproduct-vista.md) | Activates the product by depositing an Offline Confirmation Identifier for this product when performing a telephone activation.<br/> |
| [**UninstallProductKey**](uninstallproductkey-softwarelicensingproduct-vista.md)                   | Uninstalls the product key. <br/>                                                                                                    |



 

### Properties

The **SoftwareLicensingProduct** class has these properties.

<dl> <dt>

**ApplicationID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the ID of current product application.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the product description.

</dd> <dt>

**EvaluationEndDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the expiration date of this product application. After this date, the **LicenseStatus** property is set to Unlicensed and cannot be activated.

</dd> <dt>

**GracePeriodRemaining**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the remaining time, in minutes, before the parent application goes into notification mode. For volume clients, this is the remaining time before reactivation is required.

</dd> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Specifies the product identifier.

</dd> <dt>

**LicenseDependsOn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the dependency identifier for the set of SKUs used to determine license relationships for add-ons.

</dd> <dt>

**LicenseFamily**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the group identifier for the SKU used to determine license relationships for add-ons.

</dd> <dt>

**LicenseIsAddon**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates **TRUE** if the product is identified as an add-on license.

</dd> <dt>

**LicenseStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the license status of this product application. The following values are possible.



| Value                            | Description                |
|----------------------------------|----------------------------|
| <span id="0"></span>0<br/> | Unlicensed<br/>      |
| <span id="1"></span>1<br/> | Licensed<br/>        |
| <span id="2"></span>2<br/> | OOBGrace<br/>        |
| <span id="3"></span>3<br/> | OOTGrace<br/>        |
| <span id="4"></span>4<br/> | NonGenuineGrace<br/> |
| <span id="5"></span>5<br/> | Notification<br/>    |



 

</dd> <dt>

**LicenseStatusReason**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the license status. Provides additional information about why a computer is in a specific licensing state.

</dd> <dt>

**MachineURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the software licensing server URL for the binding certificate.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the product name.

</dd> <dt>

**OfflineInstallationId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the offline installation identifier of this product application. Used for offline activation. Returns a **null** value if a product key is not installed.

</dd> <dt>

**PartialProductKey**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the last five characters of the product key. Returns a **null** value if a product key is not installed.

</dd> <dt>

**ProcessorURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Software licensing server URL for the process certificate

</dd> <dt>

**ProductKeyID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the product key ID. Returns a **null** value if a product key is not installed.

</dd> <dt>

**ProductKeyURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the software licensing server URL for the product certificate.

</dd> <dt>

**UseLicenseURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the software licensing server URL for the user license.

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| End of client support<br/>    | Windows Vista<br/>                                                             |
| End of server support<br/>    | Windows Server 2008<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>SLWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SLWmi.dll</dt> </dl> |



 

 




