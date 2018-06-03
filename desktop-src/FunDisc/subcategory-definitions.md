---
Description: Each Function Discovery category may have one or more associated subcategories to provide another level of categorization.
ms.assetid: 9793e37d-6c12-431f-95d6-fd5350f11029
title: Subcategory Definitions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Subcategory Definitions

\[Function Discovery is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Each Function Discovery category may have one or more associated subcategories to provide another level of categorization. Similarly, subcategories may also have one or more associated subcategories. The result is the potential for deeply nested category hierarchies.

The following subcategories are associated with the FCTN\_CATEGORY\_DEVICES category of devices.



| Constant                                                                                                                                                                                                              | Description          |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| <span id="FCTN_SUBCAT_DEVICES_WSDPRINTERS"></span><span id="fctn_subcat_devices_wsdprinters"></span><dl> <dt>**FCTN\_SUBCAT\_DEVICES\_WSDPRINTERS**</dt> </dl> | Not used.<br/> |



The following subcategories are associated with the FCTN\_CATEGORY\_NETWORKDEVICES category of devices.



| Constant                                                                                                                                                                                                              | Description                   |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|
| <span id="FCTN_SUBCAT_NETWORKDEVICES_SSDP"></span><span id="fctn_subcat_networkdevices_ssdp"></span><dl> <dt>**FCTN\_SUBCAT\_NETWORKDEVICES\_SSDP**</dt> </dl> | The SSDP provider.<br/> |
| <span id="FCTN_SUBCAT_NETWORKDEVICES_WSD"></span><span id="fctn_subcat_networkdevices_wsd"></span><dl> <dt>**FCTN\_SUBCAT\_NETWORKDEVICES\_WSD**</dt> </dl>    | The WSD provider.<br/>  |



The following subcategories are associated with the FCTN\_CATEGORY\_REGISTRY category of devices.



| Constant                                                                                                                                                                                                  | Description                          |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------|
| <span id="FCTN_SUBCAT_REG_DIRECTED"></span><span id="fctn_subcat_reg_directed"></span><dl> <dt>**FCTN\_SUBCAT\_REG\_DIRECTED**</dt> </dl>          | Not used.<br/>                 |
| <span id="FCTN_SUBCAT_REG_PUBLICATION"></span><span id="fctn_subcat_reg_publication"></span><dl> <dt>**FCTN\_SUBCAT\_REG\_PUBLICATION**</dt> </dl> | The publication provider.<br/> |



## Remarks

Providers can define and use their own subcategories. Not all providers use subcategories.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>FunctionDiscoveryCategories.h</dt> </dl> |



## See also

<dl> <dt>

[Category Definitions](category-definitions.md)
</dt> <dt>

[Built-in Providers](built-in-providers.md)
</dt> </dl>

 

 




