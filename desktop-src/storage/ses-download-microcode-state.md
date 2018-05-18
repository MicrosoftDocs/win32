---
title: SES\_DOWNLOAD\_MICROCODE\_STATE enumeration
description: TBD.
ms.assetid: '5edff312-8373-4d36-b93c-c35fe8c2996a'
keywords: ["SES_DOWNLOAD_MICROCODE_STATE enumeration Storage Devices", "PSES_DOWNLOAD_MICROCODE_STATE enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SES_DOWNLOAD_MICROCODE_STATE
api_location:
- scsi.h
api_type:
- HeaderDef
---

# SES\_DOWNLOAD\_MICROCODE\_STATE enumeration

TBD

## Syntax


```C++
typedef enum _SES_DOWNLOAD_MICROCODE_STATE { 
  SesDownloadMcStateNoneInProgress              =  0x00,
  SesDownloadMcStateInProgress                  =  0x01,
  SesDownloadMcStateCompletedPendingReset       =  0x11,
  SesDownloadMcStateCompletedPendingPowerOn     = 0x12,
  SesDownloadMcStateCompletedPendingActivation  = 0x13
} SES_DOWNLOAD_MICROCODE_STATE, *PSES_DOWNLOAD_MICROCODE_STATE;
```



## Constants

<dl> <dt>

<span id="SesDownloadMcStateNoneInProgress"></span><span id="sesdownloadmcstatenoneinprogress"></span><span id="SESDOWNLOADMCSTATENONEINPROGRESS"></span>**SesDownloadMcStateNoneInProgress**
</dt> <dd>

Specifies no microcode download operation is in progress.

</dd> <dt>

<span id="SesDownloadMcStateInProgress"></span><span id="sesdownloadmcstateinprogress"></span><span id="SESDOWNLOADMCSTATEINPROGRESS"></span>**SesDownloadMcStateInProgress**
</dt> <dd>

Specifies a microcode download operation is in progress.

</dd> <dt>

<span id="SesDownloadMcStateCompletedPendingReset"></span><span id="sesdownloadmcstatecompletedpendingreset"></span><span id="SESDOWNLOADMCSTATECOMPLETEDPENDINGRESET"></span>**SesDownloadMcStateCompletedPendingReset**
</dt> <dd>

Specifies a microcode download operations completed and is waiting for a hard reset.

</dd> <dt>

<span id="SesDownloadMcStateCompletedPendingPowerOn"></span><span id="sesdownloadmcstatecompletedpendingpoweron"></span><span id="SESDOWNLOADMCSTATECOMPLETEDPENDINGPOWERON"></span>**SesDownloadMcStateCompletedPendingPowerOn**
</dt> <dd>

Specifies a microcode download operations completed and is waiting for a power on.

</dd> <dt>

<span id="SesDownloadMcStateCompletedPendingActivation"></span><span id="sesdownloadmcstatecompletedpendingactivation"></span><span id="SESDOWNLOADMCSTATECOMPLETEDPENDINGACTIVATION"></span>**SesDownloadMcStateCompletedPendingActivation**
</dt> <dd>

Specifies a microcode download operations completed and is waiting for activation.

</dd> </dl>

## Requirements



|                    |                                                                                                                      |
|--------------------|----------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows 10, version 1709 and later versions of Windows.<br/>                                      |
| Header<br/>  | <dl> <dt>Scsi.h (include Minitape.h or Storport.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SES_DOWNLOAD_MICROCODE_STATE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





