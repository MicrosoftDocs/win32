---
title: How To Index Multiple Output Streams
description: In shader model 5, a geometry shader can support up to 4 separate streams. This means a single shader can output between one and four output streams, depending on the number of streams declared.
ms.assetid: 2ddde992-6746-4033-9190-bde7d7b14add
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# How To: Index Multiple Output Streams

In shader model 5, a geometry shader can support up to 4 separate streams. This means a single shader can output between one and four output streams, depending on the number of streams declared.

To index multiple output streams

1.  Define a data stream using a stream template type.

    ```
        inout PointStream<OutVertex1> myStream1, 
    ```

    

2.  Define a second data stream using a stream template type.

    ```
        inout PointStream<OutVertex2> myStream2 )
    ```

    

3.  Output data to either (or both) streams using the stream output object intrinsic functions (such as Append or RestartStrip).

    ```
    void MyGS( 
        InVertex verts[2], 
        inout PointStream<OutVertex1> myStream1, 
        inout PointStream<OutVertex2> myStream2 )
    {
        OutVertex1 myVert1 = TransformVertex1( verts[0] );
        OutVertex2 myVert2 = TransformVertex2( verts[1] );
        myStream1.Append( myVert1 );
        myStream2.Append( myVert2 );
    }
    ```

    

When using a single output stream, you can emit triangle strips, line strips, or point lists. When you store triangle and line strips in the stream out buffer, they are expanded to triangle and line lists respectively. You can also rasterize one stream and not send it to a memory buffer.

When using multiple output streams, all streams must contain points, and up to one output stream can be sent to the rasterizer. More commonly, an application will not rasterize any stream.

After you stream data to a buffer, you can use that data to render any primitive type, not just the primitive type that you used to fill the buffer.

The total output of the geometry shader is limited to 1024 scalars. When multiple streams exist, the number of scalars is computed from the largest stream type multiplied by the maximum vertex count.



 Differences between shader model 4 and shader model 5:<br /> Shader model 4:<br /><ul><li>Maximum number of scalars for stream output is 64.</li><li>The per-component register mask must match across the index range.</li></ul>Shader model 5:<br /><ul><li>Maximum number of scalars for stream output is 128.</li><li>The per-component register mask does not need to match across the index range.</li><li>Dynamic indexing of outputs must be legal across all streams.</li><li>Interpolation modes do not need to match for the streams.</li></ul>

## Related topics

<dl> <dt>

[Geometry Shader Features](overviews-direct3d-11-hlsl-gs-features.md)
</dt> </dl>

 

 





