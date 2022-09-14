---
title: Using the Image Element
description: This article describes using the Image element in VML, a feature that is deprecated as of Windows Internet Explorer 9.
ms.assetid: 444c0b21-35f0-4e2d-ab6d-87a88229d9d2
keywords:
- Web workshop,image element
- designing Web pages,image element
- Vector Markup Language (VML),image element
- VML (Vector Markup Language),image element
- vector graphics,image element
- image element
- VML elements,image
- VML shapes,image element
- Vector Markup Language (VML),crop property attributes
- VML (Vector Markup Language),crop property attributes
- vector graphics,crop property attributes
- VML shapes,crop property attributes
- crop property attributes
- Vector Markup Language (VML),gain property attribute
- VML (Vector Markup Language),gain property attribute
- vector graphics,gain property attribute
- VML shapes,gain property attribute
- gain property attribute
- Vector Markup Language (VML),contrast
- VML (Vector Markup Language),contrast
- vector graphics,contrast
- VML shapes,contrast
- Vector Markup Language (VML),blacklevel property attribute
- VML (Vector Markup Language),blacklevel property attribute
- vector graphics,blacklevel property attribute
- VML shapes,blacklevel property attribute
- blacklevel property attribute
- Vector Markup Language (VML),brightness
- VML (Vector Markup Language),brightness
- vector graphics,brightness
- VML shapes,brightness
- Vector Markup Language (VML),grayscale property attribute
- VML (Vector Markup Language),grayscale property attribute
- vector graphics,grayscale property attribute
- VML shapes,grayscale property attribute
- grayscale property attribute
- Vector Markup Language (VML),gamma property attribute
- VML (Vector Markup Language),gamma property attribute
- vector graphics,gamma property attribute
- VML shapes,gamma property attribute
- gamma property attribute
ms.topic: article
ms.date: 05/31/2018
---

# Using the Image Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Using `<image>`

In this topic, we will illustrate how to use the `<image>` element to display pictures with various special effects.

If you wanted to display a picture that was loaded from an external source, you would usually use the `<img>` element provided in HTML, and then point the **src** property attribute to the location of the image file.

Alternatively you can use the `<image>` element provided in VML. When you use the `<image>` element, you can create only one image file and then display the image differently by altering the property attributes of the `<image>` element. Also, the `<image>` element provides several special effects that you can't do by simply using the `<img>` element of HTML, such as [cropping](#crop), [contrast](#contrast), [brightness](#brightness), [gamma](#gamma), and [grayscale](#grayscale).

[![back to top](images/top.gif) Back to top](#top)

## crop

You can use the **cropbottom**, **croptop**, **cropleft**, and **cropright** property attributes of the `<image>` element to display different pictures that are cropped from the same image file.

The value of these crop attributes represents the percentage cut from the edge of the picture. The value can be any number between 0 to 1. By default, the value is set to 0, indicating no crop from the edge. The value 0.1 indicates a cropping of 10 percent from the edge, The value 0.15 indicates a cropping of 15 percent from the edge, and so on.

For example, to display five pictures that are all cropped from the same image file, you can use the `<image>` element and specify different crop values, as shown in the following VML representation:

![image1.jpg (5770 bytes)](images/image1.jpg)![image1\-2.jpg (1969 bytes)](images/image1-2.jpg)![image1\-3.jpg (1148 bytes)](images/image1-3.jpg)![image1\-4.jpg (1686 bytes)](images/image1-4.jpg)![image1\-5.jpg (1364 bytes)](images/image1-5.jpg)


```HTML
<v:image style='width:100pt;height:80pt' src="image1.jpg" />
<v:image style='width:85pt;height:64pt' src="image1.jpg"
cropbottom="0.2" cropright="0.15"/>
<v:image style='width:50pt;height:44pt' src="image1.jpg"
cropbottom="0.45" cropleft="0.5"/>
<v:image style='width:80pt;height:56pt' src="image1.jpg"
croptop="0.3" cropright="0.2"/>
<v:image style='width:70pt;height:48pt' src="image1.jpg"
croptop="0.4" cropleft="0.3"/>
```





The first image, `<v:image style='width:100pt;height:80pt' src="image1.jpg" />`, doesn't have any crop value. Therefore, 100 percent of the original image is displayed at a size of 100 points by 80 points.

The second image, `<v:image style='width:85pt;height:64pt' src="image1.jpg" cropbottom="0.2" cropright="0.15"/>`, has some crop values. `cropbottom="0.2"` indicates that 20 percent of the picture will be cropped from the bottom; `cropright="0.15"` indicates that 15 percent of the picture will be cropped from the right edge. The remaining picture is then displayed at a size of 85 points by 64 points.

Similarly the third, fourth, and fifth images have some crop values. The original picture is cropped according to the crop values, and is then displayed according to the value of width and height.

[![back to top](images/top.gif) Back to top](#top)

## contrast

You can use the **gain** property attribute of the `<image>` element to display various pictures that have different contrast settings.

The value of the **gain** property attribute can be any number. By default, the value is 1, indicating the use of the same contrast as the original image. The value 0 indicates no contrast. The larger the number, the higher the contrast.

For example, to display five pictures that have different contrast settings, you can use the `<image>` element and set a different value for the **gain** property attribute, as shown in the following VML representation:

![image1.jpg (5770 bytes)](images/image1.jpg)![image2\-2.jpg (270 bytes)](images/image2-2.jpg)![image2\-3.jpg (1919 bytes)](images/image2-3.jpg)![image2\-4.jpg (3143 bytes)](images/image2-4.jpg)![image2\-5.jpg (1724 bytes)](images/image2-5.jpg)


```HTML
<v:image style='width:100pt;height:80pt' src="image1.jpg" />
<v:image style='width:100pt;height:80pt' src="image1.jpg" gain=0 />
<v:image style='width:100pt;height:80pt' src="image1.jpg" gain=0.5 />
<v:image style='width:100pt;height:80pt' src="image1.jpg" gain=3 />
<v:image style='width:100pt;height:80pt' src="image1.jpg" gain=-0.4 />
```





When the **gain** property attribute is set to 0, the entire image becomes gray because there is no contrast. The contrast is more noticeable when the **gain** property attribute is set to 3 than when it is set to 0.5. The contrast is reversed when the **gain** property attribute is set to a negative value such as -0.4.

[![back to top](images/top.gif) Back to top](#top)

## brightness

You can use the **blacklevel** property attribute of the `<image>` element to display various pictures that have different brightness settings.

The value of the **blacklevel** property attribute can be any value between 0 to 1. By default, the value is 0, indicating that the level of brightness in the original image is preserved. The value 1 indicates the highest level of brightness.

For example, to display five pictures that have different brightness settings, you can use the `<image>` element and set a different value for the **blacklevel** property attribute, as shown in the following VML representation:

![image1.jpg (5770 bytes)](images/image1.jpg)![image3\-2.jpg (2579 bytes)](images/image3-2.jpg)![image3\-3.jpg (2330 bytes)](images/image3-3.jpg)![image3\-4.jpg (2727 bytes)](images/image3-4.jpg)![image3\-5.jpg (2435 bytes)](images/image3-5.jpg)


```HTML
<v:image style='width:100pt;height:80pt' src="image1.jpg" />
<v:image style='width:100pt;height:80pt' src="image1.jpg" blacklevel=0.1 />
<v:image style='width:100pt;height:80pt' src="image1.jpg" blacklevel=0.2 />
<v:image style='width:100pt;height:80pt' src="image1.jpg" blacklevel=-0.05 />
<v:image style='width:100pt;height:80pt' src="image1.jpg" blacklevel=-0.15 />
```





[![back to top](images/top.gif) Back to top](#top)

## grayscale

You can use the **grayscale** property attribute of the `<image>` element to display pictures with or without grayscale.

The value of the **grayscale** property attribute can be either true or false. By default, the value is set to false so that the image will be displayed in color. If the value is set to true, the image will be displayed in grayscale.

For example, as shown in the following picture, the first image uses the default setting (false)of the grayscale attribute (`<v:image style='width:100pt;height:80pt' src="image1.jpg" />` ). Therefore, the picture is displayed in color.

The second image sets the grayscale attribute to true (`<v:image style='width:100pt;height:80pt' src="image1.jpg" grayscale=true />` ). Therefore, the picture is displayed in grayscale, as shown in the following VML representation:

![image1.jpg (5770 bytes)](images/image1.jpg)![image4\-2.jpg (2138 bytes)](images/image4-2.jpg)


```HTML
<v:image style='width:100pt;height:80pt' src="image1.jpg" />
<v:image style='width:100pt;height:80pt' src="image1.jpg"
grayscale=true />
```





[![back to top](images/top.gif) Back to top](#top)

## gamma

You can use the **gamma** property attribute of the `<image>` element to display pictures that have different gamma settings.

The value of the gamma property attribute can be any value between 0 and 1. By default, the value is set to 1.

For example, to display three pictures that have different gamma settings, you can use the `<image>` element and set a different value of the **gamma** property attribute, as shown in the following VML representation:

![image5\-1.jpg (2714 bytes)](images/image5-1.jpg)![image5\-2.jpg (2729 bytes)](images/image5-2.jpg)![image5\-3.jpg (2726 bytes)](images/image5-3.jpg)


```HTML
<v:image style='width:100pt;height:80pt' src="image1.jpg" />
<v:image style='width:100pt;height:80pt' src="image1.jpg" gamma=0 />
<v:image style='width:100pt;height:80pt' src="image1.jpg" gamma=0.5 />
```





For more information about this element, see the [VML specification](https://www.w3.org/TR/NOTE-VML#-toc416858408) .

 

 