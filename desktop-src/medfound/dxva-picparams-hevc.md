---
description: Provides the picture-level parameters of a compressed picture for HEVC video decoding.
ms.assetid: F73AE9CD-5BBC-4A9F-8D05-707AD5E2E92A
title: DXVA_PicParams_HEVC structure (Dxva.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DXVA_PicParams_HEVC
api_type: 
- HeaderDef
api_location: 
- dxva.h
---

# DXVA\_PicParams\_HEVC structure

Provides the picture-level parameters of a compressed picture for HEVC video decoding.

## Syntax


```C++
typedef struct _DXVA_PicParams_HEVC {
  USHORT             PicWidthInMinCbsY;
  USHORT             PicHeightInMinCbsY;
  union {
    struct {
      USHORT chroma_format_idc  :2;
      USHORT separate_colour_plane_flag   :1;
      USHORT bit_depth_luma_minus8   :3;
      USHORT bit_depth_chroma_minus8  :3;
      USHORT log2_max_pic_order_cnt_lsb_minus4  :4;
      USHORT NoPicReorderingFlag   :1;
      USHORT  NoBiPredFlag   :1;
      USHORT ReservedBits1     :1;
    };
    USHORT  wFormatAndSequenceInfoFlags;
  };
  DXVA_PicEntry_HEVC CurrPic;
  UCHAR              sps_max_dec_pic_buffering_minus1;
  UCHAR              log2_min_luma_coding_block_size_minus3;
  UCHAR              log2_diff_max_min_luma_coding_block_size;
  UCHAR              log2_min_transform_block_size_minus2;
  UCHAR              log2_diff_max_min_transform_block_size;
  UCHAR              max_transform_hierarchy_depth_inter;
  UCHAR              max_transform_hierarchy_depth_intra;
  UCHAR              num_short_term_ref_pic_sets;
  UCHAR              num_long_term_ref_pics_sps;
  UCHAR              num_ref_idx_l0_default_active_minus1;
  UCHAR              num_ref_idx_l1_default_active_minus1;
  CHAR               init_qp_minus26;
  UCHAR              ucNumDeltaPocsOfRefRpsIdx;
  USHORT             wNumBitsForShortTermRPSInSlice;
  USHORT             ReservedBits2;
  union {
    struct {
      UINT32 scaling_list_enabled_flag  :1;
      UINT32 amp_enabled_flag  :1;
      UINT32 sample_adaptive_offset_enabled_flag  :1;
      UINT32 pcm_enabled_flag   :1;
      UINT32 pcm_sample_bit_depth_luma_minus1   :4;
      UINT32 pcm_sample_bit_depth_chroma_minus1     :4;
      UINT32 log2_min_pcm_luma_coding_block_size_minus3    :2;
      UINT32 log2_diff_max_min_pcm_luma_coding_block_size  :2;
      UINT32 pcm_loop_filter_disabled_flag  :1;
      UINT32 long_term_ref_pics_present_flag   :1;
      UINT32 sps_temporal_mvp_enabled_flag  :1;
      UINT32 strong_intra_smoothing_enabled_flag   :1;
      UINT32 dependent_slice_segments_enabled_flag    :1;
      UINT32 output_flag_present_flag   :1;
      UINT32 num_extra_slice_header_bits    :3;
      UINT32 sign_data_hiding_enabled_flag  :1;
      UINT32 cabac_init_present_flag  :1;
      UINT32 ReservedBits3    :5;
    };
    UINT32             dwCodingParamToolFlags;
    union {
      struct {
        UINT32 constrained_intra_pred_flag  :1;
        UINT32 transform_skip_enabled_flag  :1;
        UINT32 cu_qp_delta_enabled_flag  :1;
        UINT32 pps_slice_chroma_qp_offsets_present_flag  :1;
        UINT32 weighted_pred_flag  :1;
        UINT32 weighted_bipred_flag  :1;
        UINT32 transquant_bypass_enabled_flag  :1;
        UINT32 tiles_enabled_flag   :1;
        UINT32 entropy_coding_sync_enabled_flag   :1;
        UINT32 uniform_spacing_flag    :1;
        UINT32 loop_filter_across_tiles_enabled_flag   :1;
        UINT32 pps_loop_filter_across_slices_enabled_flag  :1;
        UINT32 deblocking_filter_override_enabled_flag  :1;
        UINT32 pps_deblocking_filter_disabled_flag  :1;
        UINT32 lists_modification_present_flag  :1;
        UINT32 slice_segment_header_extension_present_flag  :1;
        UINT32 IrapPicFlag  :1;
        UINT32 IdrPicFlag     :1;
        UINT32 IntraPicFlag   :1;
        UINT32 ReservedBits4     :13;
      };
      UINT32   dwCodingSettingPicturePropertyFlags;
    };
    CHAR               pps_cb_qp_offset;
    CHAR               pps_cr_qp_offset;
    UCHAR              num_tile_columns_minus1;
    UCHAR              num_tile_rows_minus1;
    USHORT             column_width_minus1[19];
    USHORT             row_height_minus1[21];
    UCHAR              diff_cu_qp_delta_depth;
    CHAR               pps_beta_offset_div2;
    CHAR               pps_tc_offset_div2;
    UCHAR              log2_parallel_merge_level_minus2;
    INT                CurrPicOrderCntVal;
    DXVA_PicEntry_HEVC RefPicList[15];
    UCHAR              ReservedBits5;
    INT                PicOrderCntValList[15];
    UCHAR              RefPicSetStCurrBefore[8];
    UCHAR              RefPicSetStCurrAfter[8];
    UCHAR              RefPicSetLtCurr[8];
    USHORT             ReservedBits6;
    USHORT             ReservedBits7;
    UINT               StatusReportFeedbackNumber;
  };
} DXVA_PicParams_HEVC, *PDXVA_PicParams_HEVC;
```



## Members

<dl> <dt>

**PicWidthInMinCbsY**
</dt> <dd></dd> <dt>

**PicHeightInMinCbsY**
</dt> <dd></dd> <dt>

**chroma\_format\_idc**
</dt> <dd></dd> <dt>

**separate\_colour\_plane\_flag** 
</dt> <dd></dd> <dt>

**bit\_depth\_luma\_minus8** 
</dt> <dd></dd> <dt>

**bit\_depth\_chroma\_minus8**
</dt> <dd></dd> <dt>

**log2\_max\_pic\_order\_cnt\_lsb\_minus4**
</dt> <dd></dd> <dt>

**NoPicReorderingFlag** 
</dt> <dd></dd> <dt>

 **NoBiPredFlag** 
</dt> <dd></dd> <dt>

**ReservedBits1** 
</dt> <dd></dd> <dt>

**wFormatAndSequenceInfoFlags**
</dt> <dd></dd> <dt>

**CurrPic**
</dt> <dd></dd> <dt>

**sps\_max\_dec\_pic\_buffering\_minus1**
</dt> <dd></dd> <dt>

**log2\_min\_luma\_coding\_block\_size\_minus3**
</dt> <dd></dd> <dt>

**log2\_diff\_max\_min\_luma\_coding\_block\_size**
</dt> <dd></dd> <dt>

**log2\_min\_transform\_block\_size\_minus2**
</dt> <dd></dd> <dt>

**log2\_diff\_max\_min\_transform\_block\_size**
</dt> <dd></dd> <dt>

**max\_transform\_hierarchy\_depth\_inter**
</dt> <dd></dd> <dt>

**max\_transform\_hierarchy\_depth\_intra**
</dt> <dd></dd> <dt>

**num\_short\_term\_ref\_pic\_sets**
</dt> <dd></dd> <dt>

**num\_long\_term\_ref\_pics\_sps**
</dt> <dd></dd> <dt>

**num\_ref\_idx\_l0\_default\_active\_minus1**
</dt> <dd></dd> <dt>

**num\_ref\_idx\_l1\_default\_active\_minus1**
</dt> <dd></dd> <dt>

**init\_qp\_minus26**
</dt> <dd></dd> <dt>

**ucNumDeltaPocsOfRefRpsIdx**
</dt> <dd></dd> <dt>

**wNumBitsForShortTermRPSInSlice**
</dt> <dd></dd> <dt>

**ReservedBits2**
</dt> <dd></dd> <dt>

**scaling\_list\_enabled\_flag**
</dt> <dd></dd> <dt>

**amp\_enabled\_flag**
</dt> <dd></dd> <dt>

**sample\_adaptive\_offset\_enabled\_flag**
</dt> <dd></dd> <dt>

**pcm\_enabled\_flag** 
</dt> <dd></dd> <dt>

**pcm\_sample\_bit\_depth\_luma\_minus1** 
</dt> <dd></dd> <dt>

**pcm\_sample\_bit\_depth\_chroma\_minus1** 
</dt> <dd></dd> <dt>

**log2\_min\_pcm\_luma\_coding\_block\_size\_minus3** 
</dt> <dd></dd> <dt>

**log2\_diff\_max\_min\_pcm\_luma\_coding\_block\_size**
</dt> <dd></dd> <dt>

**pcm\_loop\_filter\_disabled\_flag**
</dt> <dd></dd> <dt>

**long\_term\_ref\_pics\_present\_flag** 
</dt> <dd></dd> <dt>

**sps\_temporal\_mvp\_enabled\_flag**
</dt> <dd></dd> <dt>

**strong\_intra\_smoothing\_enabled\_flag** 
</dt> <dd></dd> <dt>

**dependent\_slice\_segments\_enabled\_flag** 
</dt> <dd></dd> <dt>

**output\_flag\_present\_flag** 
</dt> <dd></dd> <dt>

**num\_extra\_slice\_header\_bits** 
</dt> <dd></dd> <dt>

**sign\_data\_hiding\_enabled\_flag**
</dt> <dd></dd> <dt>

**cabac\_init\_present\_flag**
</dt> <dd></dd> <dt>

**ReservedBits3** 
</dt> <dd></dd> <dt>

**dwCodingParamToolFlags**
</dt> <dd></dd> <dt>

**constrained\_intra\_pred\_flag**
</dt> <dd></dd> <dt>

**transform\_skip\_enabled\_flag**
</dt> <dd></dd> <dt>

**cu\_qp\_delta\_enabled\_flag**
</dt> <dd></dd> <dt>

**pps\_slice\_chroma\_qp\_offsets\_present\_flag**
</dt> <dd></dd> <dt>

**weighted\_pred\_flag**
</dt> <dd></dd> <dt>

**weighted\_bipred\_flag**
</dt> <dd></dd> <dt>

**transquant\_bypass\_enabled\_flag**
</dt> <dd></dd> <dt>

**tiles\_enabled\_flag** 
</dt> <dd></dd> <dt>

**entropy\_coding\_sync\_enabled\_flag** 
</dt> <dd></dd> <dt>

**uniform\_spacing\_flag** 
</dt> <dd></dd> <dt>

**loop\_filter\_across\_tiles\_enabled\_flag** 
</dt> <dd></dd> <dt>

**pps\_loop\_filter\_across\_slices\_enabled\_flag**
</dt> <dd></dd> <dt>

**deblocking\_filter\_override\_enabled\_flag**
</dt> <dd></dd> <dt>

**pps\_deblocking\_filter\_disabled\_flag**
</dt> <dd></dd> <dt>

**lists\_modification\_present\_flag**
</dt> <dd></dd> <dt>

**slice\_segment\_header\_extension\_present\_flag**
</dt> <dd></dd> <dt>

**IrapPicFlag**
</dt> <dd></dd> <dt>

**IdrPicFlag** 
</dt> <dd></dd> <dt>

**IntraPicFlag** 
</dt> <dd></dd> <dt>

**ReservedBits4** 
</dt> <dd></dd> <dt>

**dwCodingSettingPicturePropertyFlags**
</dt> <dd></dd> <dt>

**pps\_cb\_qp\_offset**
</dt> <dd></dd> <dt>

**pps\_cr\_qp\_offset**
</dt> <dd></dd> <dt>

**num\_tile\_columns\_minus1**
</dt> <dd></dd> <dt>

**num\_tile\_rows\_minus1**
</dt> <dd></dd> <dt>

**column\_width\_minus1**
</dt> <dd></dd> <dt>

**row\_height\_minus1**
</dt> <dd></dd> <dt>

**diff\_cu\_qp\_delta\_depth**
</dt> <dd></dd> <dt>

**pps\_beta\_offset\_div2**
</dt> <dd></dd> <dt>

**pps\_tc\_offset\_div2**
</dt> <dd></dd> <dt>

**log2\_parallel\_merge\_level\_minus2**
</dt> <dd></dd> <dt>

**CurrPicOrderCntVal**
</dt> <dd></dd> <dt>

**RefPicList**
</dt> <dd></dd> <dt>

**ReservedBits5**
</dt> <dd></dd> <dt>

**PicOrderCntValList**
</dt> <dd></dd> <dt>

**RefPicSetStCurrBefore**
</dt> <dd></dd> <dt>

**RefPicSetStCurrAfter**
</dt> <dd></dd> <dt>

**RefPicSetLtCurr**
</dt> <dd></dd> <dt>

**ReservedBits6**
</dt> <dd></dd> <dt>

**ReservedBits7**
</dt> <dd></dd> <dt>

**StatusReportFeedbackNumber**
</dt> <dd></dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                           |
| Header<br/>                   | <dl> <dt>Dxva.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Structures](media-foundation-structures.md)
</dt> </dl>

 

 




