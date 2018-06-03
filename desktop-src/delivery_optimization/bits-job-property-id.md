---
title: BITS\_JOB\_PROPERTY\_ID enumeration
description: The BITS\_JOB\_PROPERTY\_ID enumeration specifies the ID of the property for the DO job. This enumeration is used in the BITS\_JOB\_PROPERTY\_VALUE union to determine the type of value contained in the union.
ms.assetid: B0F3C6C2-474F-4FD8-990A-770FAA993550
keywords:
- BITS_JOB_PROPERTY_ID enumeration
topic_type:
- apiref
api_name:
- BITS_JOB_PROPERTY_ID
api_location:
- deliveryoptimization.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# BITS\_JOB\_PROPERTY\_ID enumeration

The **BITS\_JOB\_PROPERTY\_ID** enumeration specifies the ID of the property for the DO job. This enumeration is used in the [**BITS\_JOB\_PROPERTY\_VALUE**](bits-job-property-value-.md) union to determine the type of value contained in the union.

## Syntax


```C++
typedef enum  { 
  BITS_JOB_PROPERTY_ID_COST_FLAGS                     = 1,
  BITS_JOB_PROPERTY_NOTIFICATION_CLSID                = 2,
  BITS_JOB_PROPERTY_DYNAMIC_CONTENT                   = 3,
  BITS_JOB_PROPERTY_HIGH_PERFORMANCE                  = 4,
  BITS_JOB_PROPERTY_MAX_DOWNLOAD_SIZE                 = 5,
  BITS_JOB_PROPERTY_USE_STORED_CREDENTIALS            = 7,
  BITS_JOB_PROPERTY_MINIMUM_NOTIFICATION_INTERVAL_MS  = 9,
  BITS_JOB_PROPERTY_ON_DEMAND_MODE                    = 10
} BITS_JOB_PROPERTY_ID;
```



## Constants

<dl> <dt>

<span id="BITS_JOB_PROPERTY_ID_COST_FLAGS"></span><span id="bits_job_property_id_cost_flags"></span>**BITS\_JOB\_PROPERTY\_ID\_COST\_FLAGS**
</dt> <dd>

The ID that is used to [control transfer behavior](https://www.bing.com/search?q=control transfer behavior) over cellular and/or similar networks. This property may be changed while a transfer is ongoing   the new cost flags will take effect immediately.

This property uses the **BITS\_JOB\_PROPERTY\_VALUE** s **Dword** field.

</dd> <dt>

<span id="BITS_JOB_PROPERTY_NOTIFICATION_CLSID"></span><span id="bits_job_property_notification_clsid"></span>**BITS\_JOB\_PROPERTY\_NOTIFICATION\_CLSID**
</dt> <dd>

The ID that is used to [register a COM callback](https://www.bing.com/search?q=register a COM callback) by CLSID to receive notifications about the progress and completion of a DO job. The CLSID must refer to a class associated with a registered out-of-process COM server. It may also be set to **GUID\_NULL** to clear a previously set notification CLSID.

This property uses the **BITS\_JOB\_PROPERTY\_VALUE** s **CLsID** field.

</dd> <dt>

<span id="BITS_JOB_PROPERTY_DYNAMIC_CONTENT"></span><span id="bits_job_property_dynamic_content"></span>**BITS\_JOB\_PROPERTY\_DYNAMIC\_CONTENT**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="BITS_JOB_PROPERTY_HIGH_PERFORMANCE"></span><span id="bits_job_property_high_performance"></span>**BITS\_JOB\_PROPERTY\_HIGH\_PERFORMANCE**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="BITS_JOB_PROPERTY_MAX_DOWNLOAD_SIZE"></span><span id="bits_job_property_max_download_size"></span>**BITS\_JOB\_PROPERTY\_MAX\_DOWNLOAD\_SIZE**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="BITS_JOB_PROPERTY_USE_STORED_CREDENTIALS"></span><span id="bits_job_property_use_stored_credentials"></span>**BITS\_JOB\_PROPERTY\_USE\_STORED\_CREDENTIALS**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="BITS_JOB_PROPERTY_MINIMUM_NOTIFICATION_INTERVAL_MS"></span><span id="bits_job_property_minimum_notification_interval_ms"></span>**BITS\_JOB\_PROPERTY\_MINIMUM\_NOTIFICATION\_INTERVAL\_MS**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="BITS_JOB_PROPERTY_ON_DEMAND_MODE"></span><span id="bits_job_property_on_demand_mode"></span>**BITS\_JOB\_PROPERTY\_ON\_DEMAND\_MODE**
</dt> <dd>

Not supported.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl> |



## See also

<dl> <dt>

[**BITS\_JOB\_PROPERTY\_ID**](bits-job-property-id.md)
</dt> <dt>

[**BITS\_JOB\_PROPERTY\_VALUE**](bits-job-property-value-.md)
</dt> <dt>

[**BITS\_JOB\_TRANSFER\_POLICY**](bits-job-transfer-policy-.md)
</dt> <dt>

[**IBackgroundCopyJob5::SetProperty**](ibackgroundcopyjob5-setproperty.md)
</dt> <dt>

[**IBackgroundCopyJob5::GetProperty**](ibackgroundcopyjob5-getproperty.md)
</dt> </dl>

 

 





