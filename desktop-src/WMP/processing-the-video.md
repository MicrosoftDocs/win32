---
title: Processing the Video
description: Processing the Video
ms.assetid: 2fa337dd-34c0-4a09-8c20-21f6103627dd
keywords:
- Windows Media Player plug-ins,video DSP
- plug-ins,video DSP
- digital signal processing plug-ins,video processing
- DSP plug-ins,video processing
- video DSP plug-ins,processing
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Processing the Video

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The details of processing video vary for each format; it is beyond the scope of this documentation to provide these details. In a general sense, the goal of the plug-in is to change the color data in the input buffer and then copy the data to the output buffer.

The sample plug-in processes two types of video formats: YUV and RGB.

For YUV video, the red and blue color information is encoded in the U and V values and the luminance level is represented by the Y value; the green value is encoded and can be recovered by using an algorithm. The sample plug-in simply changes the U and V values to affect the color level. Each U or V byte has a value between zero and 255. The plug-in first adjusts each value to be represented by a range from -128 to 127, and then scales the value by the supplied scale factor. Finally, the code adjusts the value again for the original zero-to-255 range and copies the data to the output buffer. The following example code processes UYVY video. In this format, every other byte is a U or Y value.


```C++
while( dwHeight-- )
{
    DWORD x = dwWidth; 

        while( x-- )
        {
        // Scale the U and V bytes to 128.
        // Just copy the Y bytes.
        if( x%2 )
        {
            pbTarget[x] = pbSource[x];
        }
        else
        {
            long temp = (long)((pbSource[x] - 128) * m_fScaleFactor);

            // Truncate if exceeded full scale.
            if (temp > 127)
            temp = 127;
            if (temp < -128)
            temp = -128;

            pbTarget[x] = temp + 128;
        }
    }

    // Move the pointers to the next row.
    pbSource += lStrideIn;
    pbTarget += lStrideOut;
}

```



For RGB video, the color and luminance information is encoded as separate red, green, and blue values. The sample plug-in computes the average of the three values to determine the value for gray, and then adjusts each color value by using the supplied scale factor. Once again, the values must be normalized for the -128 to 127 range before scaling. The following code from Process32Bit shows the process for RGB32:


```C++
while( dwHeight-- )
{
    RGBQUAD* pPixelIn = (RGBQUAD*)pbSource;
    RGBQUAD* pPixelOut = (RGBQUAD*)pbTarget;

    for( DWORD x = 0; x < dwWidth; x++ )
    {
    // Get the color bytes.
    long lBlue = (long) pPixelIn[x].rgbBlue;
    long lGreen = (long) pPixelIn[x].rgbGreen;
    long lRed = (long) pPixelIn[x].rgbRed;

    // Compute the average for gray.
    long lAverage = ( lBlue + lGreen + lRed ) / 3;

    // Scale the colors to the average.
    pPixelOut[x].rgbBlue = (BYTE)( ( lBlue - lAverage ) * m_fScaleFactor  + lAverage );
    pPixelOut[x].rgbGreen = (BYTE)( ( lGreen - lAverage ) * m_fScaleFactor  + lAverage );
    pPixelOut[x].rgbRed = (BYTE)( ( lRed - lAverage ) * m_fScaleFactor  + lAverage );
    pPixelOut[x].rgbReserved = pPixelIn[x].rgbReserved;
    }

    // Move the pointers to the next row.
    pbSource += lStrideIn;
    pbTarget += lStrideOut;
}

```



For more information about video formats, see the [FourCC website](../directshow/fourcc-codes.md).

## Related topics

<dl> <dt>

[**Implementing a Video DSP Plug-in**](implementing-a-video-dsp-plug-in.md)
</dt> </dl>

 

 