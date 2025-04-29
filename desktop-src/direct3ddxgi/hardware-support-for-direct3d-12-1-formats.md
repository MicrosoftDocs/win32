---
description: This section specifies the formats ([**DXGI_FORMAT_***](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format) values) that are supported in Direct3D Feature Level 12.1 hardware.
ms.assetid: 0DC50FF3-3193-4F3B-9976-EE504C6FCC87
title: Format support for Direct3D Feature Level 12.1 hardware
ms.topic: reference
ms.date: 02/28/2025
---

# Format support for Direct3D Feature Level 12.1 hardware

This section specifies the formats ([**DXGI_FORMAT_***](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format) values) that are supported in Direct3D Feature Level 12.1 hardware.

This topic contains a section per format. A format *target* (the tables contain one row per target) can be a resource type, an HLSL intrinsic function, or a particular functionality that is dependent on a particular format.

## Format notes

The purpose of the format can change from one hardware feature level to the next.

- <sup>L</sup> : typeless format
- <sup>PCS</sup> : partially typed, castable and simple layout
- <sup>FCS</sup> : fully typed, castable and simple layout
- <sup>FNS</sup> : fully typed, non-castable and simple layout
- <sup>PCC</sup> : partially typed, castable and complex layout
- <sup>FCC</sup> : fully typed, castable and complex layout
- <sup>FNC</sup> : fully typed, non-castable and complex layout
- <sup>V</sup> : video format

To programmatically verify format support in D3D11 and D3D12, refer to [Checking hardware feature support](checking-hardware-feature-support.md).

> [!NOTE]
> The numbers of the formats are mostly, but not all, in ascending numerical order&mdash;some are out of numerical order, and listed alongside other relevant formats. Note also that *typeless* in a format name can mean *partially* typed, and not strictly typeless.

## DXGI_FORMAT_UNKNOWN<sup>L</sup> (0)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 0 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ❌ Disallowed or not available. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ❌ Disallowed or not available. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ✔️ Hardware support required. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R32G32B32A32_TYPELESS<sup>PCS</sup> (1)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R32G32B32A32_FLOAT<sup>FCS</sup> (2)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ✔️ Hardware support required. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ❔ Hardware support optional; format might be hardware accelerated. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R32G32B32A32_UINT<sup>FCS</sup> (3)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ✔️ Hardware support required. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ✔️ Hardware support required. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ❔ Hardware support optional; format might be hardware accelerated. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R32G32B32A32_SINT<sup>FCS</sup> (4)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ✔️ Hardware support required. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ❔ Hardware support optional; format might be hardware accelerated. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R32G32B32_TYPELESS<sup>PCS</sup> (5)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 96 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_R32G32B32_FLOAT<sup>FCS</sup> (6)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 96 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ✔️ Hardware support required. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❔ Hardware support optional; format might be hardware accelerated. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❔ Hardware support optional; format might be hardware accelerated. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❔ Hardware support optional; format might be hardware accelerated. |
| RenderTarget | ❔ Hardware support optional; format might be hardware accelerated. |
| Blendable RenderTarget | 〰️ Required if a related optional feature is supported. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | 〰️ Required if a related optional feature is supported. |
| 8x Multisample RenderTarget | 〰️ Required if a related optional feature is supported. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_R32G32B32_UINT<sup>FCS</sup> (7)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 96 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ✔️ Hardware support required. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❔ Hardware support optional; format might be hardware accelerated. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ✔️ Hardware support required. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | 〰️ Required if a related optional feature is supported. |
| 8x Multisample RenderTarget | 〰️ Required if a related optional feature is supported. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_R32G32B32_SINT<sup>FCS</sup> (8)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 96 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ✔️ Hardware support required. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❔ Hardware support optional; format might be hardware accelerated. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | 〰️ Required if a related optional feature is supported. |
| 8x Multisample RenderTarget | 〰️ Required if a related optional feature is supported. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_R16G16B16A16_TYPELESS<sup>PCS</sup> (9)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16G16B16A16_FLOAT<sup>FCS</sup> (10)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ✔️ Hardware support required. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Output | ✔️ Hardware support required. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16G16B16A16_UNORM<sup>FCS</sup> (11)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16G16B16A16_UINT<sup>FCS</sup> (12)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ✔️ Hardware support required. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16G16B16A16_SNORM<sup>FCS</sup> (13)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16G16B16A16_SINT<sup>FCS</sup> (14)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R32G32_TYPELESS<sup>PCS</sup> (15)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R32G32_FLOAT<sup>FCS</sup> (16)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ✔️ Hardware support required. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R32G32_UINT<sup>FCS</sup> (17)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ✔️ Hardware support required. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ✔️ Hardware support required. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R32G32_SINT<sup>FCS</sup> (18)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ✔️ Hardware support required. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R32G8X24_TYPELESS<sup>V</sup> (19)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_D32_FLOAT_S8X24_UINT<sup>V</sup> (20)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ✔️ Hardware support required. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_R32_FLOAT_X8X24_TYPELESS<sup>V</sup> (21)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ✔️ Hardware support required. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ✔️ Hardware support required. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_X32_TYPELESS_G8X24_UINT<sup>V</sup> (22)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_R10G10B10A2_TYPELESS<sup>PCS</sup> (23)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R10G10B10A2_UNORM<sup>FCS</sup> (24)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ✔️ Hardware support required. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Output | ✔️ Hardware support required. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ✔️ Hardware support required. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R10G10B10A2_UINT<sup>FCS</sup> (25)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ✔️ Hardware support required. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM<sup>FCS</sup> (89)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ❌ Disallowed or not available. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ✔️ Hardware support required. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Output | ✔️ Hardware support required. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ✔️ Hardware support required. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R11G11B10_FLOAT<sup>FNS</sup> (26)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8G8B8A8_TYPELESS<sup>PCS</sup> (27)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8G8B8A8_UNORM<sup>FCS</sup> (28)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ✔️ Hardware support required. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Output | ✔️ Hardware support required. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ✔️ Hardware support required. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8G8B8A8_UNORM_SRGB<sup>FCS</sup> (29)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ✔️ Hardware support required. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Output | ✔️ Hardware support required. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ✔️ Hardware support required. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8G8B8A8_UINT<sup>FCS</sup> (30)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ✔️ Hardware support required. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8G8B8A8_SNORM<sup>FCS</sup> (31)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8G8B8A8_SINT<sup>FCS</sup> (32)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16G16_TYPELESS<sup>PCS</sup> (33)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16G16_FLOAT<sup>FCS</sup> (34)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16G16_UNORM<sup>FCS</sup> (35)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16G16_UINT<sup>FCS</sup> (36)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ✔️ Hardware support required. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16G16_SNORM<sup>FCS</sup> (37)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16G16_SINT<sup>FCS</sup> (38)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R32_TYPELESS<sup>PCS</sup> (39)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ✔️ Hardware support required. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_D32_FLOAT<sup>FCS</sup> (40)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ✔️ Hardware support required. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R32_FLOAT<sup>FCS</sup> (41)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ✔️ Hardware support required. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ✔️ Hardware support required. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ✔️ Hardware support required. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ✔️ Hardware support required. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R32_UINT<sup>FCS</sup> (42)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ✔️ Hardware support required. |
| Stream Output Buffer | ✔️ Hardware support required. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ✔️ Hardware support required. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ✔️ Hardware support required. |
| UAV Atomic Bitwise Ops | ✔️ Hardware support required. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ✔️ Hardware support required. |
| UAV Atomic Exchange | ✔️ Hardware support required. |
| UAV Atomic Signed Min/Max | ✔️ Hardware support required. |
| UAV Atomic Unsigned Min/Max | ✔️ Hardware support required. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R32_SINT<sup>FCS</sup> (43)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ✔️ Hardware support required. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ✔️ Hardware support required. |
| UAV Atomic Bitwise Ops | ✔️ Hardware support required. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ✔️ Hardware support required. |
| UAV Atomic Exchange | ✔️ Hardware support required. |
| UAV Atomic Signed Min/Max | ✔️ Hardware support required. |
| UAV Atomic Unsigned Min/Max | ✔️ Hardware support required. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R24G8_TYPELESS<sup>V</sup> (44)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_D24_UNORM_S8_UINT<sup>V</sup> (45)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ✔️ Hardware support required. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_R24_UNORM_X8_TYPELESS<sup>V</sup> (46)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ✔️ Hardware support required. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ✔️ Hardware support required. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_X24_TYPELESS_G8_UINT<sup>V</sup> (47)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_R8G8_TYPELESS<sup>PCS</sup> (48)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8G8_UNORM<sup>FCS</sup> (49)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8G8_UINT<sup>FCS</sup> (50)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ✔️ Hardware support required. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8G8_SNORM<sup>FCS</sup> (51)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8G8_SINT<sup>FCS</sup> (52)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16_TYPELESS<sup>PCS</sup> (53)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16_FLOAT<sup>FCS</sup> (54)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_D16_UNORM<sup>FCS</sup> (55)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ✔️ Hardware support required. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16_UNORM<sup>FCS</sup> (56)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ✔️ Hardware support required. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ✔️ Hardware support required. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16_UINT<sup>FCS</sup> (57)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ✔️ Hardware support required. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ✔️ Hardware support required. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16_SNORM<sup>FCS</sup> (58)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R16_SINT<sup>FCS</sup> (59)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8_TYPELESS<sup>PCS</sup> (60)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8_UNORM<sup>FCS</sup> (61)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8_UINT<sup>FCS</sup> (62)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ✔️ Hardware support required. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8_SNORM<sup>FCS</sup> (63)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8_SINT<sup>FCS</sup> (64)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ✔️ Hardware support required. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_A8_UNORM<sup>FNS</sup> (65)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R9G9B9E5_SHAREDEXP<sup>FNC</sup> (67)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_R8G8_B8G8_UNORM<sup>FNC</sup> (68)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_G8R8_G8B8_UNORM<sup>FNC</sup> (69)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_BC1_TYPELESS<sup>PCC</sup> (70)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC1_UNORM <sup>FCC</sup> (71)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC1_UNORM_SRGB <sup>FCC</sup> (72)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC2_TYPELESS<sup>PCC</sup> (73)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC2_UNORM <sup>FCC</sup> (74)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC2_UNORM_SRGB <sup>FCC</sup> (75)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC3_TYPELESS<sup>PCC</sup> (76)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC3_UNORM <sup>FCC</sup> (77)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC3_UNORM_SRGB <sup>FCC</sup> (78)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC4_TYPELESS<sup>PCC</sup> (79)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC4_UNORM <sup>FCC</sup> (80)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC4_SNORM <sup>FCC</sup> (81)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC5_TYPELESS<sup>PCC</sup> (82)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC5_UNORM <sup>FCC</sup> (83)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC5_SNORM <sup>FCC</sup> (84)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_B5G6R5_UNORM<sup>FNS</sup> (85)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❔ Hardware support optional; format might be hardware accelerated. |
| Input Assembler Vertex Buffer | ❔ Hardware support optional; format might be hardware accelerated. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Typed Store | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ✔️ Hardware support required. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_B5G5R5A1_UNORM<sup>FNS</sup> (86)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❔ Hardware support optional; format might be hardware accelerated. |
| Input Assembler Vertex Buffer | ❔ Hardware support optional; format might be hardware accelerated. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❔ Hardware support optional; format might be hardware accelerated. |
| RenderTarget | ❔ Hardware support optional; format might be hardware accelerated. |
| Blendable RenderTarget | ❔ Hardware support optional; format might be hardware accelerated. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Typed Store | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Typed Load | ❔ Hardware support optional; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❔ Hardware support optional; format might be hardware accelerated. |
| 8x Multisample RenderTarget | ❔ Hardware support optional; format might be hardware accelerated. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ❔ Hardware support optional; format might be hardware accelerated. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_B8G8R8A8_TYPELESS<sup>PCS</sup> (90)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_B8G8R8A8_UNORM<sup>FCS</sup> (87)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❔[**12**] Hardware support optional for Direct3D 12; format might be hardware accelerated. |
| UAV Typed Store | ❔[**12**] Hardware support optional for Direct3D 12; format might be hardware accelerated. |
| UAV Typed Load | ❔[**12**] Hardware support optional for Direct3D 12; format might be hardware accelerated. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ✔️ Hardware support required. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Output | ✔️ Hardware support required. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ✔️ Hardware support required. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_B8G8R8A8_UNORM_SRGB<sup>FCS</sup> (91)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ✔️ Hardware support required. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Output | ✔️ Hardware support required. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ✔️ Hardware support required. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_B8G8R8X8_TYPELESS<sup>PCS</sup> (92)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_B8G8R8X8_UNORM<sup>FCS</sup> (88)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ✔️ Hardware support required. |
| Input Assembler Vertex Buffer | ✔️ Hardware support required. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Output | ❔ Hardware support optional; format might be hardware accelerated. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_B8G8R8X8_UNORM_SRGB<sup>FCS</sup> (93)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ✔️ Hardware support required. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ✔️ Hardware support required. |
| 8x Multisample RenderTarget | ✔️ Hardware support required. |
| Other Multisample Count RT | ❔ Hardware support optional; format might be hardware accelerated. |
| Multisample Resolve | ✔️ Hardware support required. |
| Multisample Load | ✔️ Hardware support required. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC6H_TYPELESS<sup>PCC</sup> (94)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC6H_UF16 <sup>FCC</sup> (95)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC6H_SF16 <sup>FCC</sup> (96)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC7_TYPELESS<sup>PCC</sup> (97)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC7_UNORM <sup>FCC</sup> (98)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_BC7_UNORM_SRGB <sup>FCC</sup> (99)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 128 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ✔️ Hardware support required. |
| TextureCube | ✔️ Hardware support required. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ✔️ Hardware support required. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ❌ Disallowed or not available. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ✔️ Hardware support required. |

## DXGI_FORMAT_AYUV<sup>V</sup> (100)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ✔️ Hardware support required. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Input | ✔️ Hardware support required. |
| Video Processor Output | ❔ Hardware support optional; format might be hardware accelerated. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_Y410<sup>V</sup> (101)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ❌ Disallowed or not available. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Input | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Output | ❔ Hardware support optional; format might be hardware accelerated. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_Y416<sup>V</sup> (102)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 64 |
| Format Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ✔️ Hardware support required. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Input | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Output | ❔ Hardware support optional; format might be hardware accelerated. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_NV12<sup>V</sup> (103)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ❌ Disallowed or not available. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ✔️ Hardware support required. |
| Video Processor Input | ✔️ Hardware support required. |
| Video Processor Output | ✔️ Hardware support required. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_P010<sup>V</sup> (104)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ❌ Disallowed or not available. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Input | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Output | ❔ Hardware support optional; format might be hardware accelerated. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_P016<sup>V</sup> (105)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ❌ Disallowed or not available. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Input | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Output | ❔ Hardware support optional; format might be hardware accelerated. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_420_OPAQUE<sup>V</sup> (106)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ❌ Disallowed or not available. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ❌ Disallowed or not available. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ✔️ Hardware support required. |
| Video Processor Input | ✔️ Hardware support required. |
| Video Processor Output | ✔️ Hardware support required. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_YUY2<sup>V</sup> (107)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ✔️ Hardware support required. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ❌ Disallowed or not available. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Input | ✔️ Hardware support required. |
| Video Processor Output | ❔ Hardware support optional; format might be hardware accelerated. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_Y210<sup>V</sup> (108)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ❌ Disallowed or not available. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Input | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Output | ❔ Hardware support optional; format might be hardware accelerated. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_Y216<sup>V</sup> (109)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 32 |
| Format Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ❌ Disallowed or not available. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Input | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Output | ❔ Hardware support optional; format might be hardware accelerated. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_NV11<sup>V</sup> (110)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ✔️ Hardware support required. |
| Shader sample (any filter) | ✔️ Hardware support required. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ✔️ Hardware support required. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ❌ Disallowed or not available. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ✔️ Hardware support required. |
| Blendable RenderTarget | ✔️ Hardware support required. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ✔️ Hardware support required. |
| UAV Typed Store | ✔️ Hardware support required. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Input | ❔ Hardware support optional; format might be hardware accelerated. |
| Video Processor Output | ❔ Hardware support optional; format might be hardware accelerated. |
| Shared Resource | ✔️ Hardware support required. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_AI44<sup>V</sup> (111)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ❌ Disallowed or not available. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ✔️ Hardware support required. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_IA44<sup>V</sup> (112)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ❌ Disallowed or not available. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ✔️ Hardware support required. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_P8<sup>V</sup> (113)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 8 |
| Format Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ❌ Disallowed or not available. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ✔️ Hardware support required. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |

## DXGI_FORMAT_A8P8<sup>V</sup> (114)
| Target | Support |
| - | - |
| Bits Per Element (BPE) | 16 |
| Format Support | ❔ Hardware support optional; format might be hardware accelerated. |
| Buffer | ❌ Disallowed or not available. |
| Input Assembler Vertex Buffer | ❌ Disallowed or not available. |
| Input Assembler Index Buffer | ❌ Disallowed or not available. |
| Stream Output Buffer | ❌ Disallowed or not available. |
| Texture1D | ❌ Disallowed or not available. |
| Texture2D | ✔️ Hardware support required. |
| Texture3D | ❌ Disallowed or not available. |
| TextureCube | ❌ Disallowed or not available. |
| Shader ld | ❌ Disallowed or not available. |
| Shader sample (any filter) | ❌ Disallowed or not available. |
| Shader sample_c (comparison filter) | ❌ Disallowed or not available. |
| Shader sample (mono 1_bit_filter) | ❌ Disallowed or not available. |
| Shader gather4 | ❌ Disallowed or not available. |
| Shader gather4_c | ❌ Disallowed or not available. |
| Mipmap | ❌ Disallowed or not available. |
| Mipmap Auto- Generation | ❌ Disallowed or not available. |
| RenderTarget | ❌ Disallowed or not available. |
| Blendable RenderTarget | ❌ Disallowed or not available. |
| Output Merger Logic Op | ❌ Disallowed or not available. |
| Depth/Stencil Target | ❌ Disallowed or not available. |
| Raw UAV and SRV | ❌ Disallowed or not available. |
| Structured UAV and SRV | ❌ Disallowed or not available. |
| Typed UAV | ❌ Disallowed or not available. |
| UAV Typed Store | ❌ Disallowed or not available. |
| UAV Typed Load | ❌ Disallowed or not available. |
| UAV Atomic Add | ❌ Disallowed or not available. |
| UAV Atomic Bitwise Ops | ❌ Disallowed or not available. |
| UAV Atomic Cmp&Store/ Cmp&Exch | ❌ Disallowed or not available. |
| UAV Atomic Exchange | ❌ Disallowed or not available. |
| UAV Atomic Signed Min/Max | ❌ Disallowed or not available. |
| UAV Atomic Unsigned Min/Max | ❌ Disallowed or not available. |
| CPU Lockable | ✔️ Hardware support required. |
| 4x Multisample RenderTarget | ❌ Disallowed or not available. |
| 8x Multisample RenderTarget | ❌ Disallowed or not available. |
| Other Multisample Count RT | ❌ Disallowed or not available. |
| Multisample Resolve | ❌ Disallowed or not available. |
| Multisample Load | ❌ Disallowed or not available. |
| Display Scan-Out | ❌ Disallowed or not available. |
| Cast Within Bit Layout | ❌ Disallowed or not available. |
| Video Decoder Support | ❌ Disallowed or not available. |
| Video Processor Input | ✔️ Hardware support required. |
| Video Processor Output | ❌ Disallowed or not available. |
| Shared Resource | ❌ Disallowed or not available. |
| BackBuffer Castable Even Fully Typed | ❌ Disallowed or not available. |
| Tiled Resource | ❌ Disallowed or not available. |


## DXGI_FORMAT_Related topics

[Direct3D 12 hardware feature levels](../direct3d12/hardware-feature-levels.md)

[Programming guide for DXGI](dx-graphics-dxgi-overviews.md)
