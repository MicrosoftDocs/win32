---
Description: Implementing IWICDevelopRaw
ms.assetid: '08371790-b23b-4d2e-9aea-b2c95c854401'
title: Implementing IWICDevelopRaw
---

# Implementing IWICDevelopRaw

## IWICDevelopRaw

The [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md) interface exposes processing options specific to raw image processing. All raw codecs must support the **IWICDevelopRaw** interface. Some raw codecs may not be able to support every setting exposed by this interface, but you should support all the settings that your codec is capable of performing. At minimum, every raw codec must implement the [**SetRotation**](-wic-codec-iwicdevelopraw-setrotation.md) and [**SetRenderMode**](-wic-codec-iwicdevelopraw-setrendermode.md) methods.

Additionally, some methods and interfaces that are optional for other codecs are strongly recommended for raw codecs. These include the [**GetPreview**](-wic-codec-iwicbitmapdecoder-getpreview.md) and [**GetThumbnail**](-wic-codec-iwicbitmapdecoder-getthumbnail.md) methods on the container-level decoder class, and the [**IWICBitmapSourceTransform**](-wic-codec-iwicbitmapsourcetransform.md) interface on the frame-level decode class.

Settings set by using the [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md) methods should be persisted by the codec in a way that’s consistent with the way other metadata is persisted, but you should never overwrite the original "As Shot" settings. By persisting the metadata and implementing [**LoadParameterSet**](-wic-codec-iwicdevelopraw-loadparameterset.md) and [**GetCurrentParameterSet**](-wic-codec-iwicdevelopraw-getcurrentparameterset.md), you enable raw processing applications to retrieve and apply processing settings across sessions.

A main purpose of the [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md) interface is to enable application developers to build a user interface for adjusting raw parameters that will work as consistently as possible across different codecs. Assume that an end user will adjust the parameters by using a slider control, with its minimum and maximum values mapped to the minimum and maximum ranges for the parameter. To support this, you should make every effort to treat all parameter ranges as linear. To ensure that the slider controls aren’t overly sensitive, you should also support as broad a range as possible for each parameter, covering at least 50 percent of the maximum possible range. For example, if the maximum possible range of contrast is from pure gray to pure black and white, with the default value being mapped to 0.0, the minimum range supported by a codec would be from at least halfway between the default value and pure gray on the low end (–1.0), to at least halfway between the default value and pure black and white on the high end (+1.0).


```C++
interface IWICDevelopRaw : IWICBitmapFrameDecode
{
   HRESULT QueryRawCapabilitiesInfo ( WICRawCapabilitiesInfo *pInfo );
   HRESULT LoadParameterSet ( WICRawParameterSet ParameterSet );
   HRESULT GetCurrentParameterSet ( IPropertyBag2 **ppCurrentParameterSet );
   HRESULT SetExposureCompensation ( double ev );
   HRESULT GetExposureCompensation ( double *pEV );
   HRESULT SetWhitePointRGB ( UINT Red, UINT Green, UINT Blue );
   HRESULT GetWhitePointRGB ( UINT *pRed, UINT *pGreen, UINT *pBlue );
   HRESULT SetNamedWhitePoint ( WICNamedWhitePoint WhitePoint );
   HRESULT GetNamedWhitePoint ( WICNamedWhitePoint *pWhitePoint );
   HRESULT SetWhitePointKelvin ( UINT WhitePointKelvin );
   HRESULT GetWhitePointKelvin ( UINT *pWhitePointKelvin );
   HRESULT GetKelvinRangeInfo ( UINT *pMinKelvinTemp,
               UINT *pMaxKelvinTemp,
               UINT *pKelvinTempStepValue );
   HRESULT SetContrast ( double Contrast );
   HRESULT GetContrast ( double *pContrast );
   HRESULT SetGamma ( double Gamma );
   HRESULT GetGamma ( double *pGamma );
   HRESULT SetSharpness ( double Sharpness );
   HRESULT GetSharpness ( double *pSharpness );
   HRESULT SetSaturation ( double Saturation );
   HRESULT GetSaturation ( double *pSaturation );
   HRESULT SetTint ( double Tint );
   HRESULT GetTint ( double *pTint );
   HRESULT SetNoiseReduction ( double NoiseReduction );
   HRESULT GetNoiseReduction ( double *pNoiseReduction );
   HRESULT SetDestinationColorContext (const IWICColorContext *pColorContext );
   HRESULT SetToneCurve ( UINT cbToneCurveSize,
               const WICRawToneCurve *pToneCurve );
   HRESULT GetToneCurve ( UINT cbToneCurveBufferSize,
               WICRawToneCurve *pToneCurve,
               UINT *pcbActualToneCurveBufferSize );
   HRESULT SetRotation ( double Rotation );
   HRESULT GetRotation ( double *pRotation );
   HRESULT SetRenderMode ( WICRawRenderMode RenderMode );
   HRESULT GetRenderMode ( WICRawRenderMode *pRenderMode ); 
   HRESULT SetNotificationCallback ( IWICDevelopRawNotificationCallback 
               *pCallback );
}
```



-   [QueryRawCapabilitiesInfo](#queryrawcapabilitiesinfo)
-   [LoadParameterSet](#loadparameterset)
-   [GetCurrentParameterSet](#getcurrentparameterset)
-   [Set/GetExposureCompensation](#setgetexposurecompensation)
-   [Set/GetCurrentParameterRGB, Set/GetNamedWhitePoint, Set/GetwhitePointKelvin](#setgetcurrentparameterrgb-setgetnamedwhitepoint-setgetwhitepointkelvin)
-   [Set/GetContrast](#setgetcontrast)
-   [Set/GetGamma](#setgetgamma)
-   [Set/GetSharpness](#setgetsharpness)
-   [Set/GetSaturation](#setgetsaturation)
-   [Set/GetTint](#setgettint)
-   [Set/GetNoiseReduction](#setgetnoisereduction)
-   [SetDestinationColorContext](#setdestinationcolorcontext)
-   [Set/GetToneCurve](#setgettonecurve)
-   [Set/GetRotation](#setgetrotation)
-   [Set/GetRenderMode](#setgetrendermode)
-   [SetNotificationCallback](#setnotificationcallback)

### QueryRawCapabilitiesInfo

[**QueryRawCapabilitiesInfo**](-wic-codec-iwicdevelopraw-queryrawcapabilitiesinfo.md) returns the set of supported capabilities for this raw file. The [**WICRawCapabilitiesInfo**](-wic-codec-wicrawcapabilitiesinfo.md) structure is defined as follows:


```C++
struct WICRawCapabilitiesInfo
{
   UINT cbSize;
   UINT CodecMajorVersion;
   UINT CodecMinorVersion;
   WICRawCapabilities ExposureCompensationSupport;
   WICRawCapabilities ContrastSupport;
   WICRawCapabilities RGBWhitePointSupport;
   WICRawCapabilities NamedWhitePointSupport;
   UINT NamedWhitePointSupportMask;
   WICRawCapabilities KelvinWhitePointSupport;
   WICRawCapabilities GammaSupport;
   WICRawCapabilities TintSupport;
   WICRawCapabilities SaturationSupport;
   WICRawCapabilities SharpnessSupport;
   WICRawCapabilities NoiseReductionSupport;
   WICRawCapabilities DestinationColorProfileSupport;
   WICRawCapabilities ToneCurveSupport;
   WICRawRotationCapabilities RotationSupport;              
}
```



The [**WICRawCapabilities**](-wic-codec-wicrawcapabilities.md) enumeration used in this structure is defined as:


```C++
enum WICRawCapabilities 
{   
   WICRawCapabilityNotSupported,
   WICRawCapabilityGetSupported,
   WICRawCapabilityFullySupported
}
```



The final field is a [**WICRawRotationCapabilities**](-wic-codec-wicrawrotationcapabilities.md) enumeration, defined as:


```C++
enum WICRawRotationCapabilities                    
{
   WICRawRotationCapabilityNotSupported,
   WICRawRotationCapabilityGetSupported,
   WICRawRotationCapabilityNinetyDegreesSupported
   WICRawRotationCapabilityFullySupported
}
```



### LoadParameterSet

[**LoadParameterSet**](-wic-codec-iwicdevelopraw-loadparameterset.md) enables the user to specify whether to use As Shot settings, use user-adjusted settings, or request the decoder to auto-correct the image.


```C++
enum WICRawParameterSet
{
   WICAsShotParameterSet,
   WICUserAdjustedParameterSet,
   WICAutoAdjustedParameterSet
}
```



### GetCurrentParameterSet

[**GetCurrentParameterSet**](-wic-codec-iwicdevelopraw-getcurrentparameterset.md) returns an **IPropertyBag2** with the current parameter set. The caller can then pass this parameter set to the encoder to use as the encoder options.

### Set/GetExposureCompensation

[**GetExposureCompensation**](-wic-codec-iwicdevelopraw-getexposurecompensation.md) and [**SetExposureCompensation**](-wic-codec-iwicdevelopraw-setexposurecompensation.md) indicate the exposure compensation to apply to the final output. The valid range for EV is –5.0 to +5.0 stops.

### Set/GetCurrentParameterRGB, Set/GetNamedWhitePoint, Set/GetwhitePointKelvin

These functions all provide ways to get and set the white point, either as an RGB value, a preset named value, or as a Kelvin value. The acceptable range for Kelvin is 1,500 – 30,000.

### Set/GetContrast

[**GetContrast**](-wic-codec-iwicdevelopraw-getcontrast.md) and [**SetContrast**](-wic-codec-iwicdevelopraw-setcontrast.md) indicate the amount of contrast to apply to the output. The valid range to specify contrast is –1.0 to +1.0, with the default contrast being 0.0.

### Set/GetGamma

[**GetGamma**](-wic-codec-iwicdevelopraw-getgamma.md) and [**SetGamma**](-wic-codec-iwicdevelopraw-setgamma.md) indicate the Gamma to apply. The valid range for Gamma is 0.2 to 5.0, with 1.0 being the default. Gamma typically is implemented using the traditional Gamma power function (a linear power function with unity gain). Brightness is increased with increasing Gamma and decreased as Gamma approaches zero. (Note that the minimum value is non-zero, because zero would result in a divide-by-zero error in traditional Gamma calculations. The logical minimum limit is 1/max, which is why the minimum is 0.2.)

### Set/GetSharpness

[**GetSharpness**](-wic-codec-iwicdevelopraw-getsharpness.md) and [**SetSharpness**](-wic-codec-iwicdevelopraw-setsharpness.md) indicate the amount of sharpening to apply. The valid range is –1.0 to +1.0, with 0.0 being the default amount of sharpening, and –1.0 indicating no sharpening at all.

### Set/GetSaturation

[**GetSaturation**](-wic-codec-iwicdevelopraw-getsaturation.md) and [**SetSaturation**](-wic-codec-iwicdevelopraw-setsaturation.md) indicate the amount of saturation to apply. The valid range to specify saturation is –1.0 to +1.0, with 0.0 being normal saturation, –1.0 representing complete desaturation, and +1.0 representing full saturation.

### Set/GetTint

[**GetTint**](-wic-codec-iwicdevelopraw-gettint.md) and [**SetTint**](-wic-codec-iwicdevelopraw-settint.md) indicate the tint to apply, on a green/magenta bias. The valid range is –1.0 to +1.0, with green being on the negative side of the scale and magenta on the positive. The tint scale is defined as orthogonal to color temperature.

### Set/GetNoiseReduction

[**GetNoiseReduction**](-wic-codec-iwicdevelopraw-getnoisereduction.md) and [**SetNoiseReduction**](-wic-codec-iwicdevelopraw-setnoisereduction.md) indicate the amount of noise reduction to apply. The valid range to is –1.0 to +1.0, with 0.0 indicating the default amount of noise reduction, –1.0 indicating no noise reduction and +1.0 indicating maximum noise reduction.

### SetDestinationColorContext

[**SetDestinationColorContext**](-wic-codec-iwicdevelopraw-setdestinationcolorcontext.md) specifies the color profile to apply to the image. You can call [**GetColorContexts**](-wic-codec-iwicbitmapframedecode-getcolorcontexts.md) to retrieve the current color profile.

### Set/GetToneCurve

[**GetToneCurve**](-wic-codec-iwicdevelopraw-gettonecurve.md) and [**SetToneCurve**](-wic-codec-iwicdevelopraw-settonecurve.md) specify the tone curve to apply. Assume linear interpolation between points. The **pToneCurve** is a [**WICRawToneCurve**](-wic-codec-wicrawtonecurve.md) structure, which contains an array of [**WICRawToneCurvePoint**](-wic-codec-wicrawtonecurvepoint.md) structures, and a count of the number of points in the array.


```C++
struct WICRawToneCurve 
{
   UINT cPoints;
   WICRawToneCurvePoint aPoints[];
}
```



A [**WICRawToneCurvePoint**](-wic-codec-wicrawtonecurvepoint.md) contains an input value and an output value.


```C++
struct WICRawToneCurvePoint 
{
   double Input;
   double Output;
}
```



When the caller passes **NULL** in the *pToneCurve* parameter, you should pass back the required size for the [**WICRawToneCurve**](-wic-codec-wicrawtonecurve.md) in the *pcbActualToneCurveBufferSize* parameter.

### Set/GetRotation

[**GetRotation**](-wic-codec-iwicdevelopraw-getrotation.md) and [**SetRotation**](-wic-codec-iwicdevelopraw-setrotation.md) indicate the degree of rotation to apply. A rotation of 90.0 would specify a rotation of 90 degrees clockwise. (The difference between using **SetRotation** and setting rotation using the [**CopyPixels**](-wic-codec-iwicbitmapsourcetransform-copypixels.md) method is that the rotation angle set using **SetRotation** should be persisted by the codec, while setting rotation through **CopyPixels** only rotates the image in memory.

### Set/GetRenderMode

[**GetRenderMode**](-wic-codec-iwicdevelopraw-getrendermode.md) and [**SetRenderMode**](-wic-codec-iwicdevelopraw-setrendermode.md) indicate the quality level of output the caller requires. When a user is adjusting parameters, the application should display a very fast approximation of what the actual image will look like if the changes are applied. For this purpose, the image is usually displayed at screen resolution or less, rather than the actual image resolution, to provide immediate feedback to the user. This is when an application would request Draft Mode quality, so this should be very fast. When the user has made all changes, previewed them in draft mode, and decided to decode the full image with the current settings, the application requests a Best Quality decode. This is usually also requested for printing. Where a reasonable tradeoff between speed an quality is required, the application requests Normal Quality.


```C++
enum WICRawRenderMode
{
   WICRawRenderModeDraftMode,
   WICRawRenderModeNormalQuality ,
   WICRawRenderModeBestQuality
}
```



### SetNotificationCallback

[**SetNotificationCallback**](-wic-codec-iwicdevelopraw-setnotificationcallback.md) registers a callback function for the decoder to call when any of the Raw processing parameters change. The signature for the [**IWICDevelopRawNotificationCallback**](-wic-codec-iwicdeveloprawnotificationcallback.md) has only one method, called [**Notify**](-wic-codec-iwicdeveloprawnotificationcallback-notify.md). **Notify** has a single parameter, which is a mask that indicates which of the raw processing parameters have changed.


```C++
HRESULT Notify ( UINT NotificationMask );
```



An OR operation is performed on the following values for the NotificationMask.


```C++
WICRawChangeNotification_ExposureCompensation
WICRawChangeNotification_NamedWhitePoint
WICRawChangeNotification_KelvinWhitePoint
WICRawChangeNotification_RGBWhitePoint
WICRawChangeNotification_Contrast
WICRawChangeNotification_Gamma
WICRawChangeNotification_Sharpness
WICRawChangeNotification_Saturation
WICRawChangeNotification_Tint
WICRawChangeNotification_NoiseReduction
WICRawChangeNotification_DestinationColorContext
WICRawChangeNotification_ToneCurve
WICRawChangeNotification_Rotation
WICRawChangeNotification_RenderMode
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Implementing IWICBitmapSourceTransform](-wic-imp-iwicbitmapsourcetransform.md)
</dt> <dt>

[Implementing a WIC-Enabled Encoder](-wic-implementingwicencoder.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 



