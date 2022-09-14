---
title: Setting Data Unit Extensions
description: Setting Data Unit Extensions
ms.assetid: 28328c9e-8590-48b8-92b6-1c0475978246
keywords:
- Advanced Systems Format (ASF),data unit extensions
- ASF (Advanced Systems Format),data unit extensions
- data unit extensions,setting
- streams,data unit extensions
ms.topic: article
ms.date: 05/31/2018
---

# Setting Data Unit Extensions

Some streams are configured to use data unit extensions to associate supplementary data with individual samples. For more information about extended samples, see [Data Unit Extensions](data-unit-extensions.md).

Most data unit extension systems require an extension on every sample in the stream. If you do not provide an extension of the correct size, the writer will reject the sample.

To add extended data to a sample, use the [**INSSBuffer3::SetProperty**](/previous-versions/windows/desktop/api/Wmsbuffer/nf-wmsbuffer-inssbuffer3-setproperty) method. You can get information about the data unit extensions configured on a stream by using the [**IWMStreamConfig2::GetDataUnitExtensionCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmstreamconfig2-getdataunitextensioncount) and [**IWMStreamConfig2::GetDataUnitExtension**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig2-getdataunitextension) methods.

## Related topics

<dl> <dt>

[**Configuring Data Unit Extensions**](configuring-data-unit-extensions.md)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




