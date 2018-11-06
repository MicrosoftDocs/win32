---
title: Adding the ContentDistributor Attribute
description: Adding the ContentDistributor Attribute
ms.assetid: b4ba5c9b-f28f-4275-bd39-c0ad1080d122
keywords:
- Windows Media Player online stores,adding ContentDistributor attribute
- online stores,adding ContentDistributor attribute
- type 1 online stores,adding ContentDistributor attribute
- type 2 online stores,adding ContentDistributor attribute
- Windows Media Player online stores,ContentDistributor attribute
- online stores,ContentDistributor attribute
- type 1 online stores,ContentDistributor attribute
- type 2 online stores,ContentDistributor attribute
- adding ContentDistributor attribute
- ContentDistributor
ms.topic: article
ms.date: 05/31/2018
---

# Adding the ContentDistributor Attribute

When the user attempts to play online store content or to copy the content to a CD or device, Windows Media Player calls certain methods in your COM object. To do this, the Player needs a way to differentiate your content from that of other online store providers. By adding your online store key name as the value for the **ContentDistributor** (which is an alias for the Windows Media Format SDK attribute named **WM/ContentDistributor**) attribute to your Windows Media-based content, you ensure that the Player can identify the content associated with your service.

Adding a value for **ContentDistributor** also ensures that Windows Media Player will create a node in the library for content you provide. See [Library Integration](library-integration.md).

You can specify this value two ways:

-   Use the Windows Media Player object model. When you do this, Windows Media Player adds the value you specify to the library database. Eventually, the Player will also write the attribute value to the digital media file.
-   Use the Windows Media Format SDK to programmatically add the **WM/ContentDistributor** attribute. When you do this, Windows Media Player reads the attribute value and adds it to the database when the digital media file is added to the library.

When creating your online store COM object, the file attribute value you set for **ContentDistributor** and the value assigned to the constant kszContentDistributorID in YourProject.h must match exactly. Recall that you specified this constant value for your COM object when you created the project by using the project wizard. You can change this value manually. Just be sure to use a string that uniquely identifies your service.

## Using the Windows Media Player Object Model

To specify a value for **ContentDistributor** using the Windows Media Player object model, use the [Media.setItemInfo](media-setiteminfo.md) method. The following example code specifies the value "Proseware" for **ContentDistributor** for the currently playing media item:


```C++
// Retrieve the current media item.
var theMedia = Player.currentMedia;

//Test whether the media item was retrieved.
if(theMedia)
{
    // Set the ContentDistributor value.
    theMedia.setItemInfo("ContentDistributor", "Proseware");
}
```



## Using the Windows Media Format SDK

The Windows Media Player SDK includes a sample C++ file, named SetContentDistributor.cpp, which demonstrates how to use the Windows Media Format 9 Series SDK to add the **WM/ContentDistributor** attribute. You can locate this sample file in the folder named Metadata where you installed the SDK. To use this code you must follow these steps:

1.  Install the Windows Media Format 9 Series SDK and configure the runtime as described in the documentation.
2.  Create a new empty C++ project in Visual Studio and add the sample file named SetContentDistributor.cpp to the project.
3.  Add the path to the Windows Media Format 9 Series SDK Lib folders to your list of file paths. From the **Tools** menu, choose **Options**.
4.  In the **Options** dialog box, click **Projects**, and then click **VC++ Directories**.
5.  In the **Show Directories for** drop-down list box, click **Library files**.
6.  Use the buttons to add the paths to the list boxes.
7.  Open the property pages dialog box for your project. Choose **Configuration Properties**, then **Linker**, and then **Input**. Type "wmvcore.lib" in the **Additional Dependencies** text box.

The sample code creates a command-line program. The arguments you provide when running the program specify the path to the digital media file to modify and a string for the **ContentDistributor** attribute value. The code uses **IWMHeaderInfo::SetAttribute** to add the attribute to the file you specified. You can use this sample as is or use it as a starting point for your own program.

## Related topics

<dl> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> </dl>

 

 




