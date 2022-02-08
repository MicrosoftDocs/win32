# Load

Reads texel data without any filtering or sampling.

```syntax
ElementType Texture1D<ElementType>::Load(
      in  int2          location
      in  int           offset
   [, out uint          status ] );

ElementType Texture1DArray<ElementType>::Load(
      in  int3          location
      in  int           offset
   [, out uint          status ] );

ElementType Texture2D<ElementType>::Load(
      in  int3          location,
      in  int2          offset
   [, out uint          status ] );

ElementType Texture2DArray<ElementType>::Load(
      in  int4          location,
      in  int2          offset
   [, out uint          status ] );

ElementType Texture2DMS<ElementType>::Load(
      in  int2          location,
      in  int           sampleIndex,
   [, in  int2          offset ]
   [, out uint          status ] );

ElementType Texture2DMSArray<ElementType>::Load(
      in  int3          location,
      in  int           sampleIndex,
   [, in  int2          offset ]
   [, out uint          status ] );

ElementType Texture3D<ElementType>::Load(
      in  int4          location,
      in  int3          offset
   [, out uint          status ] );
```

| Parameter | Description |
| - | - |
| in [`<LocationType> location`](#locationtype-location) | The texture coordinates. This method uses a 0-based coordinate system and not a 0.0-1.0 UV system. |
| in [`<OffsetType> offset`](#offsettype-offset) | The offset applied to the texture coordinates before sampling. |
| in [`int sampleIndex`](#int-sampleindex) | The sample index. |
| out [`uint status`](#uint-status) | The status of the operation. You can't access the status directly; instead, pass the status to the CheckAccessFullyMapped intrinsic function. CheckAccessFullyMapped returns TRUE if all values from the corresponding Sample, Gather, or Load operation accessed mapped tiles in a tiled resource. If any values were taken from an unmapped tile, CheckAccessFullyMapped returns FALSE. |