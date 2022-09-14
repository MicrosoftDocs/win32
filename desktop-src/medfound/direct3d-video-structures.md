---
description: Describes the structures used by the Microsoft Direct3D 9 video interfaces.
ms.assetid: 584c087e-53f0-42d8-99ed-a0d013379363
title: Direct3D 9 Video Structures
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 9 Video Structures

Describes the structures used by the Microsoft Direct3D 9 video interfaces.



| Structure                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**D3D\_OMAC**](d3d-omac.md)<br/> Contains a Message Authentication Code (MAC).<br/>                                                                                                                                                                                                                                                                        |
| [**D3DAES\_CTR\_IV**](d3daes-ctr-iv.md)<br/> Contains an initialization vector (IV).<br/>                                                                                                                                                                                                                                                                   |
| [**D3DAUTHENTICATEDCHANNEL\_CONFIGURE\_INPUT**](d3dauthenticatedchannel-configure-input.md)<br/> Contains input data for the [**IDirect3DAuthenticatedChannel9::Configure**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-configure) method.<br/>                                                                                                                     |
| [**D3DAUTHENTICATEDCHANNEL\_CONFIGURE\_OUTPUT**](d3dauthenticatedchannel-configure-output.md)<br/> Contains the response to a call to the [**IDirect3DAuthenticatedChannel9::Configure**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-configure) method.<br/>                                                                                                        |
| [**D3DAUTHENTICATEDCHANNEL\_CONFIGUREINITIALIZE**](d3dauthenticatedchannel-configureinitialize.md)<br/> Contains input data for a [**D3DAUTHENTICATEDCONFIGURE\_INITIALIZE**](d3dauthenticatedconfigure-initialize.md) command.<br/>                                                                                                                       |
| [**D3DAUTHENTICATEDCHANNEL\_CONFIGUREPROTECTION**](d3dauthenticatedchannel-configureprotection.md)<br/> Contains input data for a [**D3DAUTHENTICATEDCONFIGURE\_PROTECTION**](d3dauthenticatedconfigure-protection.md) command.<br/>                                                                                                                       |
| [**D3DAUTHENTICATEDCHANNEL\_CONFIGURECRYPTOSESSION**](d3dauthenticatedchannel-configurecryptosession.md)<br/> Contains input data for a [**D3DAUTHENTICATEDCONFIGURE\_CRYPTOSESSION**](d3dauthenticatedconfigure-cryptosession.md) command.<br/>                                                                                                           |
| [**D3DAUTHENTICATEDCHANNEL\_CONFIGURESHAREDRESOURCE**](d3dauthenticatedchannel-configuresharedresource.md)<br/> Contains input data for a [**D3DAUTHENTICATEDCONFIGURE\_SHAREDRESOURCE**](d3dauthenticatedconfigure-sharedresource.md) command.<br/>                                                                                                       |
| [**D3DAUTHENTICATEDCHANNEL\_CONFIGUREUNCOMPRESSEDENCRYPTION**](d3dauthenticatedchannel-configureuncompressedencryption.md)<br/> Contains input data for a [**D3DAUTHENTICATEDCONFIGURE\_ENCRYPTIONWHENACCESSIBLE**](d3dauthenticatedconfigure-encryptionwhenaccessible.md) command.<br/>                                                                   |
| [**D3DAUTHENTICATEDCHANNEL\_PROTECTION\_FLAGS**](d3dauthenticatedchannel-protection-flags.md)<br/> Specifies the protection level for video content.<br/>                                                                                                                                                                                                   |
| [**D3DAUTHENTICATEDCHANNEL\_QUERY\_INPUT**](d3dauthenticatedchannel-query-input.md)<br/> Contains input data for the [**IDirect3DAuthenticatedChannel9::Query**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-query) method.<br/>                                                                                                                                     |
| [**D3DAUTHENTICATEDCHANNEL\_QUERY\_OUTPUT**](d3dauthenticatedchannel-query-output.md)<br/> Contains the response to a call to the [**IDirect3DAuthenticatedChannel9::Query**](/windows/desktop/api/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-query) method.<br/>                                                                                                                        |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYCHANNELTYPE\_OUTPUT**](d3dauthenticatedchannel-querychanneltype-output.md)<br/> Contains the response to a [**D3DAUTHENTICATEDQUERY\_CHANNELTYPE**](d3dauthenticatedquery-channeltype.md) query.<br/>                                                                                                                     |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYCRYPTOSESSION\_INPUT**](d3dauthenticatedchannel-querycryptosession-input.md)<br/> Contains input data for a [**D3DAUTHENTICATEDQUERY\_CRYPTOSESSION**](d3dauthenticatedquery-cryptosession.md) query.<br/>                                                                                                                |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYCRYPTOSESSION\_OUTPUT**](d3dauthenticatedchannel-querycryptosession-output.md)<br/> Contains the response to a [**D3DAUTHENTICATEDQUERY\_CRYPTOSESSION**](d3dauthenticatedquery-cryptosession.md) query.<br/>                                                                                                             |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYDEVICEHANDLE\_OUTPUT**](d3dauthenticatedchannel-querydevicehandle-output.md)<br/> Contains the response to a [**D3DAUTHENTICATEDQUERY\_DEVICEHANDLE**](d3dauthenticatedquery-devicehandle.md) query.<br/>                                                                                                                 |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYEVICTIONENCRYPTIONGUID\_INPUT**](d3dauthenticatedchannel-queryevictionencryptionguid-input.md)<br/> Contains input data for a [**D3DAUTHENTICATEDQUERY\_ENCRYPTIONWHENACCESSIBLEGUID**](d3dauthenticatedquery-encryptionwhenaccessibleguid.md) query.<br/>                                                                |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYEVICTIONENCRYPTIONGUID\_OUTPUT**](d3dauthenticatedchannel-queryevictionencryptionguid-output.md)<br/> Contains the response to a [**D3DAUTHENTICATEDQUERY\_ENCRYPTIONWHENACCESSIBLEGUID**](d3dauthenticatedquery-encryptionwhenaccessibleguid.md) query.<br/>                                                             |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYEVICTIONENCRYPTIONGUIDCOUNT\_OUTPUT**](d3dauthenticatedchannel-queryevictionencryptionguidcount-output.md)<br/> Contains the response to a [**D3DAUTHENTICATEDQUERY\_ENCRYPTIONWHENACCESSIBLEGUIDCOUNT**](d3dauthenticatedquery-encryptionwhenaccessibleguidcount.md) query.<br/>                                         |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYINFOBUSTYPE\_OUTPUT**](d3dauthenticatedchannel-queryinfobustype-output.md)<br/> Contains the response to a [**D3DAUTHENTICATEDQUERY\_ACCESSIBILITYATTRIBUTES**](d3dauthenticatedquery-accessibilityattributes.md) query.<br/>                                                                                             |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYOUTPUTID\_INPUT**](d3dauthenticatedchannel-queryoutputid-input.md)<br/> Contains intput data for a [**D3DAUTHENTICATEDQUERY\_OUTPUTID**](d3dauthenticatedquery-outputid.md) query.<br/>                                                                                                                                   |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYOUTPUTID\_OUTPUT**](d3dauthenticatedchannel-queryoutputid-output.md)<br/> Contains the response to a [**D3DAUTHENTICATEDQUERY\_OUTPUTID**](d3dauthenticatedquery-outputid.md) query.<br/>                                                                                                                                 |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYOUTPUTIDCOUNT\_INPUT**](d3dauthenticatedchannel-queryoutputidcount-input.md)<br/> Contains input data for a [**D3DAUTHENTICATEDQUERY\_OUTPUTIDCOUNT**](d3dauthenticatedquery-outputidcount.md) query.<br/>                                                                                                                |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYOUTPUTIDCOUNT\_OUTPUT**](d3dauthenticatedchannel-queryoutputidcount-output.md)<br/> Contains the response to a [**D3DAUTHENTICATEDQUERY\_OUTPUTIDCOUNT**](d3dauthenticatedquery-outputidcount.md) query.<br/>                                                                                                             |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYPROTECTION\_OUTPUT**](d3dauthenticatedchannel-queryprotection-output.md)<br/> Contains the response to a [**D3DAUTHENTICATEDQUERY\_PROTECTION**](d3dauthenticatedquery-protection.md) query.<br/>                                                                                                                         |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYRESTRICTEDSHAREDRESOURCEPROCESS\_INPUT**](d3dauthenticatedchannel-queryrestrictedsharedresourceprocess-input.md)<br/> Contains input data for a [**D3DAUTHENTICATEDQUERY\_RESTRICTEDSHAREDRESOURCEPROCESS**](d3dauthenticatedquery-restrictedsharedresourceprocess.md) query.<br/>                                        |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYRESTRICTEDSHAREDRESOURCEPROCESS\_OUTPUT**](d3dauthenticatedchannel-queryrestrictedsharedresourceprocess-output.md)<br/> Contains the response to a [**D3DAUTHENTICATEDQUERY\_RESTRICTEDSHAREDRESOURCEPROCESS**](d3dauthenticatedquery-restrictedsharedresourceprocess.md) query.<br/>                                     |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYRESTRICTEDSHAREDRESOURCEPROCESSCOUNT\_OUTPUT**](d3dauthenticatedchannel-queryrestrictedsharedresourceprocesscount-output.md)<br/> Contains the response to a [**D3DAUTHENTICATEDQUERY\_RESTRICTEDSHAREDRESOURCEPROCESSCOUNT**](d3dauthenticatedquery-restrictedsharedresourceprocesscount.md) query.<br/>                 |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYUNCOMPRESSEDENCRYPTIONLEVEL\_OUTPUT**](d3dauthenticatedchannel-queryuncompressedencryptionlevel-output.md)<br/> Contains the response to a [**D3DAUTHENTICATEDQUERY\_CURRENTENCRYPTIONWHENACCESSIBLE**](d3dauthenticatedquery-currentencryptionwhenaccessible.md) query.<br/>                                             |
| [**D3DAUTHENTICATEDCHANNEL\_QUERYUNRESTRICTEDPROTECTEDSHAREDRESOURCECOUNT\_OUTPUT**](d3dauthenticatedchannel-queryunrestrictedprotectedsharedresourcecount-output.md)<br/> Contains the response to a [**D3DAUTHENTICATEDQUERY\_UNRESTRICTEDPROTECTEDSHAREDRESOURCECOUNT**](d3dauthenticatedquery-unrestrictedprotectedsharedresourcecount.md) query.<br/> |
| [**D3DCONTENTPROTECTIONCAPS**](/windows/desktop/api/d3d9caps/ns-d3d9caps-d3dcontentprotectioncaps)<br/> Describes the content protection capabilities of a display driver.<br/>                                                                                                                                                                                                                    |
| [**D3DENCRYPTED\_BLOCK\_INFO**](d3dencrypted-block-info.md)<br/> Specifies which bytes are encrypted in a protected video surface.<br/>                                                                                                                                                                                                                     |
| [**D3DOVERLAYCAPS**](/windows/desktop/api/d3d9caps/ns-d3d9caps-d3doverlaycaps)<br/> Specifies hardware overlay capabilities for a Direct3D device.<br/>                                                                                                                                                                                                                                            |
| [**DXVABufferInfo**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxvabufferinfo)<br/> Specifies a buffer for the [**IDirect3DDXVADevice9::Execute**](idirect3ddxvadevice9-execute.md) method.<br/>                                                                                                                                                                                                  |
| [**DXVACompBufferInfo**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxvacompbufferinfo)<br/> Specifies the requirements for compressed surfaces for DirectX Video Acceleration (DXVA).<br/>                                                                                                                                                                                                         |
| [**DXVAUncompDataInfo**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxvauncompdatainfo)<br/> Specifies the dimensions and pixel format of the uncompressed surfaces for DXVA video decoding.<br/>                                                                                                                                                                                                   |



 

## Related topics

<dl> <dt>

[Direct3D Video APIs](direct3d-video-apis.md)
</dt> </dl>

 

 




