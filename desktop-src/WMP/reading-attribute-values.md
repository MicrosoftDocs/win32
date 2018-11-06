---
title: Reading Attribute Values
description: Reading Attribute Values
ms.assetid: 5f791f47-472e-409f-b716-2ace11f34742
keywords:
- Windows Media Player,attributes for media items
- Windows Media Player object model,attributes for media items
- object model,attributes for media items
- Windows Media Player Mobile,attributes for media items
- Windows Media Player ActiveX control,attributes for media items
- Windows Media Player Mobile ActiveX control,attributes for media items
- ActiveX control,attributes for media items
- Windows Media Player library,attributes for media items
- library,attributes for media items
- attributes,reading values
- reading attribute values
ms.topic: article
ms.date: 05/31/2018
---

# Reading Attribute Values

The attributes you can find in the library and in Windows Media files have predefined names. You can write code that retrieves the value of one attribute by passing the name of that attribute to *Media*.**getItemInfo** or *Media*.**getItemInfoByType**. You can also write code that retrieves the values of all of the attributes in a file or item.

The following C# example retrieves the value of the **Title** attribute and displays it in a message box. In this example, the **Player** object was defined as axWMPLib.AxWindowsMediaPlayer Player.


```C++
IWMPMedia media;
string strAttribValue = "";

// Initialize the media object
media = Player.currentMedia;

// Retrieve the object's Title attribute
strAttribValue = media.getItemInfo("Title");

// Display the title
if (strAttribValue != "")
{
    MessageBox.Show("Current title: " + strAttribValue);
}

```



In the call to **getItemInfoByType**, the second parameter is a string that specifies the language. If you pass an empty string as shown in this example, the method retrieves the value in the default language. For information about the third parameter, see [Attributes with Multiple Values](attributes-with-multiple-values.md).

The following C# example retrieves the values for a given attribute in the current media item. It returns these values as a semicolon-delimited string. Note that for attributes represented as objects, such as **WM/Lyrics\_Synchronised**, **WM/Picture**, and **WM/UserWebURL**, the function returns an empty string.


```C++
private string getAttributeValues(string strAttrName, IWMPMedia3 media)
{
    string strAttrValue = "";
    int iAttrCount = 0;

    if (media != null)
    {
        // Retrieve the count of values for this attribute
        iAttrCount = media.getAttributeCountByType(strAttrName, "");

        // Retrieve the values
        for (int i = 0; i < iAttrCount; i++)
        {
            strAttrValue += media.getItemInfoByType(strAttrName, "", i);
            strAttrValue += ";";
        }
    }

    // Return the resulting string
    return strAttrValue;
}

```



The third argument passed to the **getItemInfoByType** method is the index of a particular attribute in a set of attributes with the same name.

You can use similar code to retrieve attributes that have unique names. In those cases, **getAttributeCountByType** returns 1. In the example shown earlier, the call to **getItemInfoByType** would execute only once.

## Related topics

<dl> <dt>

[**Changing Attribute Values**](changing-attribute-values.md)
</dt> <dt>

[**Media Item Attributes**](media-item-attributes.md)
</dt> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**Reading Attribute Values from a CD or DVD**](reading-attribute-values-from-a-cd-or-dvd.md)
</dt> </dl>

 

 




