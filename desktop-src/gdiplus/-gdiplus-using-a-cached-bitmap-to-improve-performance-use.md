---
Description: 'Image and Bitmap objects store images in a device-independent format.'
ms.assetid: '42e2b664-197c-4c54-9220-b6231d6439d0'
title: Using a Cached Bitmap to Improve Performance
---

# Using a Cached Bitmap to Improve Performance

[**Image**](-gdiplus-class-image-class.md) and [**Bitmap**](-gdiplus-class-bitmap-class.md) objects store images in a device-independent format. A [**CachedBitmap**](-gdiplus-class-cachedbitmap-class.md) object stores an image in the format of the current display device. Rendering an image stored in a **CachedBitmap** object is fast because no processing time is spent converting the image to the format required by the display device.

The following example creates a [**Bitmap**](-gdiplus-class-bitmap-class.md) object and a [**CachedBitmap**](-gdiplus-class-cachedbitmap-class.md) object from the file Texture.jpg. The **Bitmap** and the **CachedBitmap** are each drawn 30,000 times. If you run the code, you will see that the **CachedBitmap** images are drawn substantially faster than the **Bitmap** images.


```
Bitmap        bitmap(L"Texture.jpg");
UINT          width = bitmap.GetWidth();
UINT          height = bitmap.GetHeight();
CachedBitmap  cBitmap(&amp;bitmap, &amp;graphics);
int           j, k;
for(j = 0; j < 300; j += 10)
   for(k = 0; k < 1000; ++k)
     graphics.DrawImage(&amp;bitmap, j, j / 2, width, height);
for(j = 0; j < 300; j += 10)
   for(k = 0; k < 1000; ++k)
      graphics.DrawCachedBitmap(&amp;cBitmap, j, 150 + j / 2 );
```



> [!Note]  
> A [**CachedBitmap**](-gdiplus-class-cachedbitmap-class.md) object matches the format of the display device at the time the **CachedBitmap** object was constructed. If the user of your program changes the display settings, your code should construct a new **CachedBitmap** object. The **DrawImage** method will fail if you pass it a **CachedBitmap** object that was created prior to a change in the display format.

 

 

 



