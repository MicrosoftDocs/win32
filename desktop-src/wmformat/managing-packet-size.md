---
title: Managing Packet Size
description: Managing Packet Size
ms.assetid: 75ccda39-255a-4213-824e-1ca778a741dc
keywords:
- Windows Media Format SDK,managing packet sizes
- Windows Media Format SDK,packet sizes
- profiles,packet sizes
- profiles,managing packet sizes
- packets,sizes
- packets,IWMPacketSize interface
- IWMPacketSize
ms.topic: article
ms.date: 05/31/2018
---

# Managing Packet Size

The writer is designed to manage the size of packets internally. However, you may have specific requirements for your application that call for some manual control over the size of packets in the ASF files that you write. The Windows Media Format SDK provides two interfaces, [**IWMPacketSize**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmpacketsize) and [**IWMPacketSize2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmpacketsize2) that enable you to control the maximum and minimum size of packets.

Both packet size interfaces are exposed in the profile object. They are also available to the reader object. As with other profile-related interfaces, the reader can access only the reading methods.

The size of packets has some effect on performance. In general, the smaller the packet size, the more fragmented the data is within a file. The more fragmented a file is, the less efficient it will be to reconstruct it. In a streaming scenario, this may not be an important consideration, as the process of reading a file from an Internet source is generally inefficient. When dealing with a file locally however, this might be a consideration.

## Related topics

<dl> <dt>

[**IWMPacketSize Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmpacketsize)
</dt> <dt>

[**IWMPacketSize2 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmpacketsize2)
</dt> <dt>

[**Working with Profiles**](working-with-profiles.md)
</dt> </dl>

 

 




