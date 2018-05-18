---
title: IdeHwControl routine
description: The IdeHwControl miniport driver routine notifies the miniport driver about Plug and Play (PnP) and power events.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: '53f85f8d-3b50-4cfe-8bdd-d41d8c057f3e'
keywords: ["IdeHwControl routine Storage Devices", "IDE_HW_CONTROL"]
topic_type:
- apiref
api_name:
- IdeHwControl
api_location:
- irb.h
api_type:
- UserDefined
---

# IdeHwControl routine

The *IdeHwControl* miniport driver routine notifies the miniport driver about Plug and Play (PnP) and power events.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
IDE_HW_CONTROL IdeHwControl;

BOOLEAN IdeHwControl(
  _In_    PVOID              ChannelExtension,
  _In_    IDE_CONTROL_ACTION ControlAction,
  _Inout_ PVOID              Parameters
)
{ ... }
```



## Parameters

<dl> <dt>

*ChannelExtension* \[in\]
</dt> <dd>

A pointer to the channel extension.

</dd> <dt>

*ControlAction* \[in\]
</dt> <dd>

Contains an enumerator value of type [**IDE\_CONTROL\_ACTION**](ide-control-action.md) that indicates the control action to perform.

</dd> <dt>

*Parameters* \[in, out\]
</dt> <dd>

A pointer to a buffer that contains the parameters that are associated with the control action. This parameter can have one of the values in the following table.



| Control action                  | Parameters                                                                            | Description                                                             |
|---------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **IdeStart**<br/>         | Parameter points to a structure of type IDE\_CHANNEL\_CONFIGURATION.<br/>       | Indicates that the port driver is starting the channel.<br/>      |
| **IdeVendorDefined**<br/> | Parameter points to a structure of type IDE\_VENDOR\_DEFINED\_POWER\_INFO.<br/> | Indicates that there is a vendor defined power event coming.<br/> |



 

</dd> </dl>

## Return value

*IdeHwControl* returns **TRUE** if the operation was successful. Otherwise, it returns **FALSE**.

## Remarks

The port driver makes sure that there is no outstanding I/O on the channel before it invokes this routine. The miniport driver can have its own power policy methods when the system enters a different power state. In order to achieve this, the miniport driver needs to do the following:

-   Add a power policy setting scheme into the miniport driver's INF file. A GUID is needed to present a miniport driver-defined power policy. For more information about the power settings directive, see [**INF AddPowerSetting Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546313). More information about the GUIDs can be found at [Disk settings](https://msdn.microsoft.com/library/windows/hardware/mt608265).

-   When the miniport driver routine *IdeHwControl* is called with control action **IdeStart**:<dl> Check the SupportedAdvances.AdvancedChannelConfigurationSupported field in the ChannelConfiguration structure.  
    Check the AdvancedChannelConfiguration-&gt;Present.VendorDefinedPower field in the ChannelConfiguration structure.  
    If the values of the two fields listed previously are both **TRUE**, this version of the ATA port driver supports vendor-defined power management.  
    If vendor-defined power management is supported by the ATA port driver, the miniport driver can register for special power management handling by setting the AdvancedChannelConfiguration-&gt;VendorDefinedPower.ValidGuids and AdvancedChannelConfiguration-&gt;VendorDefinedPower.Guid\[\] fields (the latter should be the GUID of the power policy in the miniport driver's INF file).  
    </dl>
-   After vendor-defined power management is registered, the miniport driver will be able to receive calls to its *IdeHwControl* routine with control action **IdeVendorDefined** when the system power scheme changes.

-   While the miniport driver processes the *IdeHwControl* routine with control action **IdeVendorDefined**, it should do following:<dl> Compare the **SettingGuid** field from the parameter field of structure IDE\_VENDOR\_DEFINED\_POWER\_INFO with the GUID that the miniport driver registered to make sure that the call is for this channel. If the GUIDs do not match, the miniport driver should complete the call and take no action.  
    Get the **Value** field from the parameter field of structure IDE\_VENDOR\_DEFINED\_POWER\_INFO and perform the appropriate miniport driver-specific power management action.  
    </dl>

## Requirements



|                            |                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>               |
| Header<br/>          | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**AtaPortGetUncachedExtension**](ataportgetuncachedextension.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IdeHwControl%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






