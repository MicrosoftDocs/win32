---
description: This section specifies the formats ([**DXGI_FORMAT_***](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format) values) that are supported in Direct3D Feature Level 12.1 hardware.
ms.assetid: 0DC50FF3-3193-4F3B-9976-EE504C6FCC87
title: Format support for Direct3D Feature Level 12.1 hardware
ms.topic: article
ms.date: 05/31/2018
---

# Format support for Direct3D Feature Level 12.1 hardware

This section specifies the formats ([**DXGI_FORMAT_***](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format) values) that are supported in Direct3D Feature Level 12.1 hardware.

The table summarizes the feature support, using the following key.

| Symbol                            | Description                                                                   |
|-----------------------------------|-------------------------------------------------------------------------------|
| **-**                             | Disallowed or not available.                                                  |
| ![required](images/letter-r.jpg)  | Hardware support is required.                                                 |
| ![optional](images/letter-o.jpg)  | Hardware support optional, the format may or may not be hardware accelerated. |
| ![dependant](images/letter-d.jpg) | Required if related optional feature is supported.                            |

This topic contains a section per format. A format *target* (the tables contain one row per target) can be a resource type, an HLSL intrinsic function, or a particular functionality that is dependent on a particular format.

To programmatically verify format support in D3D11 and D3D12, refer to [Checking hardware feature support](checking-hardware-feature-support.md).

> [!NOTE] 
> The numbers of the formats are mostly, but not all, in ascending numerical order&mdash;some are out of numerical order, and listed alongside other relevant formats. Note also that *typeless* in a format name can mean *partially* typed, and not strictly typeless (refer to the [Format notes](#format-notes) section at the end of the topic).

## DXGI_FORMAT_UNKNOWN<sup>L</sup> (0)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 0 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | \- |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | \- |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | ![required](images/letter-r.jpg) |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R32G32B32A32_TYPELESS<sup>PCS</sup> (1)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R32G32B32A32_FLOAT<sup>FCS</sup> (2)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | ![required](images/letter-r.jpg) |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![optional](images/letter-o.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R32G32B32A32_UINT<sup>FCS</sup> (3)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | ![required](images/letter-r.jpg) |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | ![required](images/letter-r.jpg) |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![optional](images/letter-o.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R32G32B32A32_SINT<sup>FCS</sup> (4)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | ![required](images/letter-r.jpg) |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![optional](images/letter-o.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R32G32B32_TYPELESS<sup>PCS</sup> (5)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 96 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_R32G32B32_FLOAT<sup>FCS</sup> (6)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 96 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | ![required](images/letter-r.jpg) |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![optional](images/letter-o.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![optional](images/letter-o.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![optional](images/letter-o.jpg) |
| RenderTarget | ![optional](images/letter-o.jpg) |
| Blendable RenderTarget | ![dependant](images/letter-d.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![dependant](images/letter-d.jpg) |
| 8x Multisample RenderTarget | ![dependant](images/letter-d.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_R32G32B32_UINT<sup>FCS</sup> (7)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 96 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | ![required](images/letter-r.jpg) |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![optional](images/letter-o.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | ![required](images/letter-r.jpg) |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![dependant](images/letter-d.jpg) |
| 8x Multisample RenderTarget | ![dependant](images/letter-d.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_R32G32B32_SINT<sup>FCS</sup> (8)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 96 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | ![required](images/letter-r.jpg) |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![optional](images/letter-o.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![dependant](images/letter-d.jpg) |
| 8x Multisample RenderTarget | ![dependant](images/letter-d.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_R16G16B16A16_TYPELESS<sup>PCS</sup> (9)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16G16B16A16_FLOAT<sup>FCS</sup> (10)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | ![required](images/letter-r.jpg) |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | ![optional](images/letter-o.jpg) |
| Video Processor Output | ![required](images/letter-r.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16G16B16A16_UNORM<sup>FCS</sup> (11)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16G16B16A16_UINT<sup>FCS</sup> (12)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | ![required](images/letter-r.jpg) |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16G16B16A16_SNORM<sup>FCS</sup> (13)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16G16B16A16_SINT<sup>FCS</sup> (14)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R32G32_TYPELESS<sup>PCS</sup> (15)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R32G32_FLOAT<sup>FCS</sup> (16)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | ![required](images/letter-r.jpg) |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R32G32_UINT<sup>FCS</sup> (17)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | ![required](images/letter-r.jpg) |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | ![required](images/letter-r.jpg) |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R32G32_SINT<sup>FCS</sup> (18)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | ![required](images/letter-r.jpg) |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R32G8X24_TYPELESS<sup>V</sup> (19)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_D32_FLOAT_S8X24_UINT<sup>V</sup> (20)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | ![required](images/letter-r.jpg) |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_R32_FLOAT_X8X24_TYPELESS<sup>V</sup> (21)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | ![required](images/letter-r.jpg) |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | ![required](images/letter-r.jpg) |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_X32_TYPELESS_G8X24_UINT<sup>V</sup> (22)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_R10G10B10A2_TYPELESS<sup>PCS</sup> (23)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R10G10B10A2_UNORM<sup>FCS</sup> (24)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | ![required](images/letter-r.jpg) |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | ![optional](images/letter-o.jpg) |
| Video Processor Output | ![required](images/letter-r.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | ![required](images/letter-r.jpg) |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R10G10B10A2_UINT<sup>FCS</sup> (25)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | ![required](images/letter-r.jpg) |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM<sup>FCS</sup> (89)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | \- |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | ![required](images/letter-r.jpg) |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | ![optional](images/letter-o.jpg) |
| Video Processor Output | ![required](images/letter-r.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | ![required](images/letter-r.jpg) |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R11G11B10_FLOAT<sup>FNS</sup> (26)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8G8B8A8_TYPELESS<sup>PCS</sup> (27)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8G8B8A8_UNORM<sup>FCS</sup> (28)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | ![required](images/letter-r.jpg) |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | ![optional](images/letter-o.jpg) |
| Video Processor Output | ![required](images/letter-r.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | ![required](images/letter-r.jpg) |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8G8B8A8_UNORM_SRGB<sup>FCS</sup> (29)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | ![required](images/letter-r.jpg) |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | ![optional](images/letter-o.jpg) |
| Video Processor Output | ![required](images/letter-r.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | ![required](images/letter-r.jpg) |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8G8B8A8_UINT<sup>FCS</sup> (30)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | ![required](images/letter-r.jpg) |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8G8B8A8_SNORM<sup>FCS</sup> (31)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8G8B8A8_SINT<sup>FCS</sup> (32)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16G16_TYPELESS<sup>PCS</sup> (33)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16G16_FLOAT<sup>FCS</sup> (34)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16G16_UNORM<sup>FCS</sup> (35)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16G16_UINT<sup>FCS</sup> (36)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | ![required](images/letter-r.jpg) |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16G16_SNORM<sup>FCS</sup> (37)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16G16_SINT<sup>FCS</sup> (38)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R32_TYPELESS<sup>PCS</sup> (39)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | ![required](images/letter-r.jpg) |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_D32_FLOAT<sup>FCS</sup> (40)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | ![required](images/letter-r.jpg) |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R32_FLOAT<sup>FCS</sup> (41)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | ![required](images/letter-r.jpg) |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | ![required](images/letter-r.jpg) |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | ![required](images/letter-r.jpg) |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | ![required](images/letter-r.jpg) |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R32_UINT<sup>FCS</sup> (42)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | ![required](images/letter-r.jpg) |
| Stream Output Buffer | ![required](images/letter-r.jpg) |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | ![required](images/letter-r.jpg) |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | ![required](images/letter-r.jpg) |
| UAV Atomic Bitwise Ops | ![required](images/letter-r.jpg) |
| UAV Atomic Cmp&Store/ Cmp&Exch | ![required](images/letter-r.jpg) |
| UAV Atomic Exchange | ![required](images/letter-r.jpg) |
| UAV Atomic Signed Min/Max | ![required](images/letter-r.jpg) |
| UAV Atomic Unsigned Min/Max | ![required](images/letter-r.jpg) |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R32_SINT<sup>FCS</sup> (43)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | ![required](images/letter-r.jpg) |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | ![required](images/letter-r.jpg) |
| UAV Atomic Bitwise Ops | ![required](images/letter-r.jpg) |
| UAV Atomic Cmp&Store/ Cmp&Exch | ![required](images/letter-r.jpg) |
| UAV Atomic Exchange | ![required](images/letter-r.jpg) |
| UAV Atomic Signed Min/Max | ![required](images/letter-r.jpg) |
| UAV Atomic Unsigned Min/Max | ![required](images/letter-r.jpg) |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R24G8_TYPELESS<sup>V</sup> (44)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_D24_UNORM_S8_UINT<sup>V</sup> (45)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | ![required](images/letter-r.jpg) |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_R24_UNORM_X8_TYPELESS<sup>V</sup> (46)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | ![required](images/letter-r.jpg) |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | ![required](images/letter-r.jpg) |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_X24_TYPELESS_G8_UINT<sup>V</sup> (47)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_R8G8_TYPELESS<sup>PCS</sup> (48)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8G8_UNORM<sup>FCS</sup> (49)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8G8_UINT<sup>FCS</sup> (50)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | ![required](images/letter-r.jpg) |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8G8_SNORM<sup>FCS</sup> (51)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8G8_SINT<sup>FCS</sup> (52)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16_TYPELESS<sup>PCS</sup> (53)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16_FLOAT<sup>FCS</sup> (54)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_D16_UNORM<sup>FCS</sup> (55)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | ![required](images/letter-r.jpg) |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16_UNORM<sup>FCS</sup> (56)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | ![required](images/letter-r.jpg) |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | ![required](images/letter-r.jpg) |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16_UINT<sup>FCS</sup> (57)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | ![required](images/letter-r.jpg) |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | ![required](images/letter-r.jpg) |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16_SNORM<sup>FCS</sup> (58)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R16_SINT<sup>FCS</sup> (59)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8_TYPELESS<sup>PCS</sup> (60)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8_UNORM<sup>FCS</sup> (61)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8_UINT<sup>FCS</sup> (62)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | ![required](images/letter-r.jpg) |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8_SNORM<sup>FCS</sup> (63)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8_SINT<sup>FCS</sup> (64)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![required](images/letter-r.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | \- |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_A8_UNORM<sup>FNS</sup> (65)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R9G9B9E5_SHAREDEXP<sup>FNC</sup> (67)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_R8G8_B8G8_UNORM<sup>FNC</sup> (68)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_G8R8_G8B8_UNORM<sup>FNC</sup> (69)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_BC1_TYPELESS<sup>PCC</sup> (70)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC1_UNORM <sup>FCC</sup> (71)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC1_UNORM_SRGB <sup>FCC</sup> (72)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC2_TYPELESS<sup>PCC</sup> (73)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC2_UNORM <sup>FCC</sup> (74)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC2_UNORM_SRGB <sup>FCC</sup> (75)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC3_TYPELESS<sup>PCC</sup> (76)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC3_UNORM <sup>FCC</sup> (77)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC3_UNORM_SRGB <sup>FCC</sup> (78)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC4_TYPELESS<sup>PCC</sup> (79)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC4_UNORM <sup>FCC</sup> (80)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC4_SNORM <sup>FCC</sup> (81)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC5_TYPELESS<sup>PCC</sup> (82)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC5_UNORM <sup>FCC</sup> (83)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC5_SNORM <sup>FCC</sup> (84)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_B5G6R5_UNORM<sup>FNS</sup> (85)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![optional](images/letter-o.jpg) |
| Input Assembler Vertex Buffer | ![optional](images/letter-o.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![optional](images/letter-o.jpg) |
| UAV Typed Store | ![optional](images/letter-o.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![required](images/letter-r.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_B5G5R5A1_UNORM<sup>FNS</sup> (86)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![optional](images/letter-o.jpg) |
| Input Assembler Vertex Buffer | ![optional](images/letter-o.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![optional](images/letter-o.jpg) |
| RenderTarget | ![optional](images/letter-o.jpg) |
| Blendable RenderTarget | ![optional](images/letter-o.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![optional](images/letter-o.jpg) |
| UAV Typed Store | ![optional](images/letter-o.jpg) |
| UAV Typed Load | ![optional](images/letter-o.jpg) |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![optional](images/letter-o.jpg) |
| 8x Multisample RenderTarget | ![optional](images/letter-o.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![optional](images/letter-o.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_B8G8R8A8_TYPELESS<sup>PCS</sup> (90)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_B8G8R8A8_UNORM<sup>FCS</sup> (87)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | ![required](images/letter-r.jpg) |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | ![optional](images/letter-o.jpg) |
| Video Processor Output | ![required](images/letter-r.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | ![required](images/letter-r.jpg) |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_B8G8R8A8_UNORM_SRGB<sup>FCS</sup> (91)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | ![required](images/letter-r.jpg) |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | ![optional](images/letter-o.jpg) |
| Video Processor Output | ![required](images/letter-r.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | ![required](images/letter-r.jpg) |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_B8G8R8X8_TYPELESS<sup>PCS</sup> (92)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_B8G8R8X8_UNORM<sup>FCS</sup> (88)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Vertex Buffer | ![required](images/letter-r.jpg) |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | ![optional](images/letter-o.jpg) |
| Video Processor Output | ![optional](images/letter-o.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_B8G8R8X8_UNORM_SRGB<sup>FCS</sup> (93)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | ![required](images/letter-r.jpg) |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| 8x Multisample RenderTarget | ![required](images/letter-r.jpg) |
| Other Multisample Count RT | ![optional](images/letter-o.jpg) |
| Multisample Resolve | ![required](images/letter-r.jpg) |
| Multisample Load | ![required](images/letter-r.jpg) |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC6H_TYPELESS<sup>PCC</sup> (94)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC6H_UF16 <sup>FCC</sup> (95)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC6H_SF16 <sup>FCC</sup> (96)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC7_TYPELESS<sup>PCC</sup> (97)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC7_UNORM <sup>FCC</sup> (98)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_BC7_UNORM_SRGB <sup>FCC</sup> (99)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | ![required](images/letter-r.jpg) |
| TextureCube | ![required](images/letter-r.jpg) |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | ![required](images/letter-r.jpg) |
| Video Decoder Support | \- |
| Video Processor Input | \- |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | ![required](images/letter-r.jpg) |

## DXGI_FORMAT_AYUV<sup>V</sup> (100)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![optional](images/letter-o.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | ![required](images/letter-r.jpg) |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | ![optional](images/letter-o.jpg) |
| Video Processor Input | ![required](images/letter-r.jpg) |
| Video Processor Output | ![optional](images/letter-o.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_Y410<sup>V</sup> (101)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![optional](images/letter-o.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | \- |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | ![optional](images/letter-o.jpg) |
| Video Processor Input | ![optional](images/letter-o.jpg) |
| Video Processor Output | ![optional](images/letter-o.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_Y416<sup>V</sup> (102)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ![optional](images/letter-o.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | ![required](images/letter-r.jpg) |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | ![optional](images/letter-o.jpg) |
| Video Processor Input | ![optional](images/letter-o.jpg) |
| Video Processor Output | ![optional](images/letter-o.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_NV12<sup>V</sup> (103)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | \- |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | ![required](images/letter-r.jpg) |
| Video Processor Input | ![required](images/letter-r.jpg) |
| Video Processor Output | ![required](images/letter-r.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_P010<sup>V</sup> (104)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![optional](images/letter-o.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | \- |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | ![optional](images/letter-o.jpg) |
| Video Processor Input | ![optional](images/letter-o.jpg) |
| Video Processor Output | ![optional](images/letter-o.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_P016<sup>V</sup> (105)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![optional](images/letter-o.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | \- |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | ![optional](images/letter-o.jpg) |
| Video Processor Input | ![optional](images/letter-o.jpg) |
| Video Processor Output | ![optional](images/letter-o.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_420_OPAQUE<sup>V</sup> (106)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | \- |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | \- |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | ![required](images/letter-r.jpg) |
| Video Processor Input | ![required](images/letter-r.jpg) |
| Video Processor Output | ![required](images/letter-r.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_YUY2<sup>V</sup> (107)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![required](images/letter-r.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | \- |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | ![optional](images/letter-o.jpg) |
| Video Processor Input | ![required](images/letter-r.jpg) |
| Video Processor Output | ![optional](images/letter-o.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_Y210<sup>V</sup> (108)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![optional](images/letter-o.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | \- |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | ![optional](images/letter-o.jpg) |
| Video Processor Input | ![optional](images/letter-o.jpg) |
| Video Processor Output | ![optional](images/letter-o.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_Y216<sup>V</sup> (109)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ![optional](images/letter-o.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | \- |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | ![optional](images/letter-o.jpg) |
| Video Processor Input | ![optional](images/letter-o.jpg) |
| Video Processor Output | ![optional](images/letter-o.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_NV11<sup>V</sup> (110)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ![optional](images/letter-o.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | ![required](images/letter-r.jpg) |
| Shader sample (any filter) | ![required](images/letter-r.jpg) |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | ![required](images/letter-r.jpg) |
| Shader gather4_c | \- |
| Mipmap | \- |
| Mipmap Auto- Generation | \- |
| RenderTarget | ![required](images/letter-r.jpg) |
| Blendable RenderTarget | ![required](images/letter-r.jpg) |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | ![required](images/letter-r.jpg) |
| UAV Typed Store | ![required](images/letter-r.jpg) |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | ![optional](images/letter-o.jpg) |
| Video Processor Input | ![optional](images/letter-o.jpg) |
| Video Processor Output | ![optional](images/letter-o.jpg) |
| Shared Resource | ![required](images/letter-r.jpg) |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_AI44<sup>V</sup> (111)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ![optional](images/letter-o.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | \- |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | \- |
| Video Processor Input | ![required](images/letter-r.jpg) |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_IA44<sup>V</sup> (112)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ![optional](images/letter-o.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | \- |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | \- |
| Video Processor Input | ![required](images/letter-r.jpg) |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_P8<sup>V</sup> (113)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ![optional](images/letter-o.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | \- |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | \- |
| Video Processor Input | ![required](images/letter-r.jpg) |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## DXGI_FORMAT_A8P8<sup>V</sup> (114)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ![optional](images/letter-o.jpg) |
| Buffer | \- |
| Input Assembler Vertex Buffer | \- |
| Input Assembler Index Buffer | \- |
| Stream Output Buffer | \- |
| Texture1D | \- |
| Texture2D | ![required](images/letter-r.jpg) |
| Texture3D | \- |
| TextureCube | \- |
| Shader ld | \- |
| Shader sample (any filter) | \- |
| Shader sample_c (comparison filter) | \- |
| Shader sample (mono 1_bit_filter) | \- |
| Shader gather4 | \- |
| Shader gather4_c | \- |
| Mipmap | \- |
| Mipmap Auto- Generation | \- |
| RenderTarget | \- |
| Blendable RenderTarget | \- |
| Output Merger Logic Op | \- |
| Depth/Stencil Target | \- |
| Raw UAV and SRV | \- |
| Structured UAV and SRV | \- |
| Typed UAV | \- |
| UAV Typed Store | \- |
| UAV Typed Load | \- |
| UAV Atomic Add | \- |
| UAV Atomic Bitwise Ops | \- |
| UAV Atomic Cmp&Store/ Cmp&Exch | \- |
| UAV Atomic Exchange | \- |
| UAV Atomic Signed Min/Max | \- |
| UAV Atomic Unsigned Min/Max | \- |
| CPU Lockable | ![required](images/letter-r.jpg) |
| 4x Multisample RenderTarget | \- |
| 8x Multisample RenderTarget | \- |
| Other Multisample Count RT | \- |
| Multisample Resolve | \- |
| Multisample Load | \- |
| Display Scan-Out | \- |
| Cast Within Bit Layout | \- |
| Video Decoder Support | \- |
| Video Processor Input | ![required](images/letter-r.jpg) |
| Video Processor Output | \- |
| Shared Resource | \- |
| BackBuffer Castable Even Fully Typed | \- |
| Tiled Resource | \- |

## Format notes

The purpose of the format can change from one hardware feature level to the next.

<dl> <dt>

<sup>L</sup> : typeless format
</dt> <dt>

<sup>PCS</sup> : partially typed, castable and simple layout
</dt> <dt>

 <sup>FCS</sup> : fully typed, castable and simple layout
</dt> <dt>

<sup>FNS</sup> : fully typed, non-castable and simple layout
</dt> <dt>

<sup>PCC</sup> : partially typed, castable and complex layout
</dt> <dt>

 <sup>FCC</sup> : fully typed, castable and complex layout
</dt> <dt>

<sup>FNC</sup> : fully typed, non-castable and complex layout
</dt> <dt>

<sup>V</sup> : video format
</dt> </dl>

## DXGI_FORMAT_Related topics

[D3D12 Hardware Feature Levels](../direct3d12/hardware-feature-levels.md)

[Programming Guide for DXGI](dx-graphics-dxgi-overviews.md)
