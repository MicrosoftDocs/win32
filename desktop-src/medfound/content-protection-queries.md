---
description: Lists the queries for the IDirect3DAuthenticatedChannel9::Query method.
ms.assetid: 75e246c6-bf23-44d9-8fb3-46a6dc5324a5
title: Content Protection Queries
ms.topic: article
ms.date: 05/31/2018
---

# Content Protection Queries

Lists the queries for the [**IDirect3DAuthenticatedChannel9::Query**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-query) method.



| Status request                                                                                                                            | Description                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**D3DAUTHENTICATEDQUERY\_ACCESSIBILITYATTRIBUTES**](d3dauthenticatedquery-accessibilityattributes.md)                                   | Returns the type of I/O bus used to send data to the GPU.                                                                                                   |
| [**D3DAUTHENTICATEDQUERY\_CHANNELTYPE**](d3dauthenticatedquery-channeltype.md)                                                           | Returns the type of authenticated channel.                                                                                                                  |
| [**D3DAUTHENTICATEDQUERY\_CRYPTOSESSION**](d3dauthenticatedquery-cryptosession.md)                                                       | Returns handles to the cryptographic session and Direct3D device that are associated with a specified DirectX Video Acceleration 2 (DXVA-2) decoder device. |
| [**D3DAUTHENTICATEDQUERY\_CURRENTENCRYPTIONWHENACCESSIBLE**](d3dauthenticatedquery-currentencryptionwhenaccessible.md)                   | Returns the encryption type that is applied before content becomes accessible to the CPU or bus.                                                            |
| [**D3DAUTHENTICATEDQUERY\_DEVICEHANDLE**](d3dauthenticatedquery-devicehandle.md)                                                         | Returns a handle to the device that is associated with this authenticated channel.                                                                          |
| [**D3DAUTHENTICATEDQUERY\_ENCRYPTIONWHENACCESSIBLEGUID**](d3dauthenticatedquery-encryptionwhenaccessibleguid.md)                         | Returns one of the encryption types that can be used to encrypt content before it becomes accessible to the CPU or bus.                                     |
| [**D3DAUTHENTICATEDQUERY\_ENCRYPTIONWHENACCESSIBLEGUIDCOUNT**](d3dauthenticatedquery-encryptionwhenaccessibleguidcount.md)               | Returns the number of encryption types that can be used to encrypt content before it becomes accessible to the CPU or bus.                                  |
| [**D3DAUTHENTICATEDQUERY\_OUTPUTID**](d3dauthenticatedquery-outputid.md)                                                                 | Returns one of the output identifiers that is associated with a specified cryptographic session and Direct3D device.                                        |
| [**D3DAUTHENTICATEDQUERY\_OUTPUTIDCOUNT**](d3dauthenticatedquery-outputidcount.md)                                                       | Returns the number of output identifiers associated with a specified cryptographic session and Direct3D device.                                             |
| [**D3DAUTHENTICATEDQUERY\_PROTECTION**](d3dauthenticatedquery-protection.md)                                                             | Returns the current protection level for the device.                                                                                                        |
| [**D3DAUTHENTICATEDQUERY\_RESTRICTEDSHAREDRESOURCEPROCESS**](d3dauthenticatedquery-restrictedsharedresourceprocess.md)                   | Returns information about a process that is allowed to open shared resources with restricted access.                                                        |
| [**D3DAUTHENTICATEDQUERY\_RESTRICTEDSHAREDRESOURCEPROCESSCOUNT**](d3dauthenticatedquery-restrictedsharedresourceprocesscount.md)         | Returns the number of processes that are allowed to open shared resources with restricted access.                                                           |
| [**D3DAUTHENTICATEDQUERY\_UNRESTRICTEDPROTECTEDSHAREDRESOURCECOUNT**](d3dauthenticatedquery-unrestrictedprotectedsharedresourcecount.md) | Returns the number of protected shared resources that can be opened by any process with no restrictions.                                                    |



 

## Related topics

<dl> <dt>

[Direct3D Video APIs](direct3d-video-apis.md)
</dt> <dt>

[GPU-Based Content Protection](gpu-based-content-protection.md)
</dt> </dl>

 

 



