---
title: Fibre Channel HBA Library Routines
description: Fibre Channel HBA Library Routines
ms.assetid: '9810e9ee-b47c-415f-a0c0-a0c58f2b203b'
keywords: ["fibre"]
---

# Fibre Channel HBA Library Routines

## 

This section includes the following fibre channel HBA library routines:

<dl>

[**HBA\_ADAPTER\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff556045)  
[**HBA\_CloseAdapter**](hba-closeadapter.md)  
[**HBA\_FreeLibrary**](hba-freelibrary.md)  
[**HBA\_GetAdapterAttributes**](hba-getadapterattributes.md)  
[**HBA\_GetAdapterName**](hba-getadaptername.md)  
[**HBA\_GetAdapterPortAttributes**](hba-getadapterportattributes.md)  
[**HBA\_GetBindingCapability**](hba-getbindingcapability.md)  
[**HBA\_GetBindingSupport**](hba-getbindingsupport.md)  
[**HBA\_GetDiscoveredPortAttributes**](hba-getdiscoveredportattributes.md)  
[**HBA\_GetEventBuffer**](hba-geteventbuffer.md)  
[**HBA\_GetFC4Statistics**](hba-getfc4statistics.md)  
[**HBA\_GetFcpPersistentBinding**](hba-getfcppersistentbinding.md)  
[**HBA\_GetFCPStatistics**](hba-getfcpstatistics.md)  
[**HBA\_GetFcpTargetMapping**](hba-getfcptargetmapping.md)  
[**HBA\_GetFcpTargetMappingV2**](hba-getfcptargetmappingv2.md)  
[**HBA\_GetNumberOfAdapters**](hba-getnumberofadapters.md)  
[**HBA\_GetPersistentBindingV2**](hba-getpersistentbindingv2.md)  
[**HBA\_GetPortAttributesByWWN**](hba-getportattributesbywwn.md)  
[**HBA\_GetPortStatistics**](hba-getportstatistics.md)  
[**HBA\_GetRNIDMgmtInfo**](hba-getrnidmgmtinfo.md)  
[**HBA\_GetVendorLibraryAttributes**](hba-getvendorlibraryattributes.md)  
[**HBA\_GetVersion**](hba-getversion.md)  
[**HBA\_GetWrapperLibraryAttributes**](hba-getwrapperlibraryattributes.md)  
[**HBA\_LINK\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff556121)  
[**HBA\_LoadLibrary**](hba-loadlibrary.md)  
[**HBA\_OpenAdapter**](hba-openadapter.md)  
[**HBA\_OpenAdapterByWWN**](hba-openadapterbywwn.md)  
[**HBA\_PORT\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff557123)  
[**HBA\_PORTSTAT\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff557117)  
[**HBA\_RefreshAdapterConfiguration**](hba-refreshadapterconfiguration.md)  
[**HBA\_RefreshInformation**](hba-refreshinformation.md)  
[**HBA\_RegisterForAdapterAddEvents**](hba-registerforadapteraddevents.md)  
[**HBA\_RegisterForAdapterEvents**](hba-registerforadapterevents.md)  
[**HBA\_RegisterForAdapterPortEvents**](hba-registerforadapterportevents.md)  
[**HBA\_RegisterForAdapterPortStatEvents**](hba-registerforadapterportstatevents.md)  
[**HBA\_RegisterForLinkEvents**](hba-registerforlinkevents.md)  
[**HBA\_RegisterForTargetEvents**](hba-registerfortargetevents.md)  
[**HBA\_RegisterLibrary**](hba-registerlibrary.md)  
[**HBA\_RegisterLibraryV2**](hba-registerlibraryv2.md)  
[**HBA\_RemoveAllPersistentBindings**](hba-removeallpersistentbindings.md)  
[**HBA\_RemoveCallback**](hba-removecallback.md)  
[**HBA\_RemovePersistentBinding**](hba-removepersistentbinding.md)  
[**HBA\_ResetStatistics**](hba-resetstatistics.md)  
[**HBA\_ScsiInquiryV2**](hba-scsiinquiryv2.md)  
[**HBA\_ScsiReadCapacityV2**](hba-scsireadcapacityv2.md)  
[**HBA\_ScsiReportLUNsV2**](hba-scsireportlunsv2.md)  
[**HBA\_SendCTPassThru**](hba-sendctpassthru.md)  
[**HBA\_SendCTPassThruV2**](hba-sendctpassthruv2.md)  
[**HBA\_SendLIRR**](hba-sendlirr.md)  
[**HBA\_SendReadCapacity**](hba-sendreadcapacity.md)  
[**HBA\_SendReportLUNs**](hba-sendreportluns.md)  
[**HBA\_SendRLS**](hba-sendrls.md)  
[**HBA\_SendRNID**](hba-sendrnid.md)  
[**HBA\_SendRNIDV2**](hba-sendrnidv2.md)  
[**HBA\_SendRPL**](hba-sendrpl.md)  
[**HBA\_SendRPS**](hba-sendrps.md)  
[**HBA\_SendScsiInquiry**](hba-sendscsiinquiry.md)  
[**HBA\_SendSRL**](hba-sendsrl.md)  
[**HBA\_SetBindingSupport**](hba-setbindingsupport.md)  
[**HBA\_SetPersistentBindingV2**](hba-setpersistentbindingv2.md)  
[**HBA\_SetRNIDMgmtInfo**](hba-setrnidmgmtinfo.md)  
[**HBA\_TARGET\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff557234)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Fibre%20Channel%20HBA%20Library%20Routines%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




