---
description: This sample demonstrates how to serialize and de-serialize ink in various formats.
ms.assetid: 468d9c2a-0b3c-4a44-a049-3f3b78e952ba
title: Ink Serialization Sample
ms.topic: article
ms.date: 05/31/2018
---

# Ink Serialization Sample

This sample demonstrates how to serialize and de-serialize ink in various formats. The application represents a form with fields for inputting first name, last name, and signature. The user may save this data as pure ink serialized format (ISF), Extensible Markup Language (XML) using base64 encoded ISF, or HTML, which references ink in a base64 encoded fortified Graphics Interchange Format (GIF) image. The application also enables the user to open files that were saved as XML and ISF formats. The ISF format uses extended properties to store the first name and last name, whereas the XML and HTML formats store this information in custom attributes.

This sample does not support loading from the HTML format, because HTML is not suitable for storing structured data. Because the data is separated into name, signature, and so on, a format that preserves this separation, such as XML or another kind of database format, is required.

HTML is very useful in an environment in which formatting is important, such as in a word processing document. The HTML that is saved by this sample uses fortified GIFs. These GIFs have ISF embedded within them, which preserves the full fidelity of the ink. A word processing application can save a document containing multiple types of data, such as images, tables, formatted text, and ink persisted in an HTML format. This HTML would render in browsers that do not recognize ink. However, when loaded into an application that is ink-enabled, the full fidelity of the original ink is available and can be rendered, edited, or used for recognition.

The following features are used in this sample:

-   The [Ink](/previous-versions/aa515768(v=msdn.10)) object's [Load](/previous-versions/ms569609(v=vs.100)) method
-   The [Ink](/previous-versions/aa515768(v=msdn.10)) object's [Save](/previous-versions/dotnet/netframework-3.5/ms571335(v=vs.90)) method
-   The [Ink](/previous-versions/aa515768(v=msdn.10)) object's [ExtendedProperties](/previous-versions/ms582214(v=vs.100)) property

## Collecting Ink

First, reference the Tablet PC API, which are installed with the Windows Vista and Windows XP Tablet PC Edition Software Development Kit (SDK).


```C++
using Microsoft.Ink;
```



The constructor creates and enables an [InkCollector](/previous-versions/ms836493(v=msdn.10)), `ic`, for the form.


```C++
ic = new InkCollector(Signature.Handle);
ic.Enabled = true;
```



## Saving a File

The `SaveAsMenu_Click` method handles the Save As dialog box, creates a file stream in which to save the ink data, and calls the save method that corresponds to the user's choice.

## Saving to an ISF File

In the `SaveISF` method, the first and last name values are added to the [ExtendedProperties](/previous-versions/ms582214(v=vs.100)) property of the [InkCollector](/previous-versions/ms836493(v=msdn.10)) object's [Ink](/previous-versions/ms836505(v=msdn.10)) property, before the ink is serialized and written to the file. After the ink has been serialized, the first and last name values are removed from the [Ink](/previous-versions/aa515768(v=msdn.10)) object's ExtendedProperties property.


```C++
byte[] isf;

// This is the ink object which is serialized
ExtendedProperties inkProperties = ic.Ink.ExtendedProperties;

// Store the name fields in the ink object
// These fields roundtrip through the ISF format
// Ignore empty fields since strictly empty strings 
//       cannot be stored in ExtendedProperties.
if (FirstNameBox.Text.Length > 0)
{
    inkProperties.Add(FirstName, FirstNameBox.Text);
}
if (LastNameBox.Text.Length > 0)
{
    inkProperties.Add(LastName, LastNameBox.Text);
}

// Perform the serialization
isf = ic.Ink.Save(PersistenceFormat.InkSerializedFormat);

// If the first and last names were added as extended
// properties to the ink, remove them - these properties
// are only used for the save and there is no need to
// keep them around on the ink object.
if (inkProperties.DoesPropertyExist(FirstName))
{
    inkProperties.Remove(FirstName);
}
if (inkProperties.DoesPropertyExist(LastName))
{
    inkProperties.Remove(LastName);
}

// Write the ISF to the stream
s.Write(isf,0,isf.Length);
```



## Saving to an XML File

In the `SaveXML` method, an [XmlTextWriter](/dotnet/api/system.xml.xmltextwriter?view=netcore-3.1&preserve-view=true) object is used to create and write to an XML document. Using the [Ink](/previous-versions/aa515768(v=msdn.10)) object's [Save](/previous-versions/dotnet/netframework-3.5/ms571335(v=vs.90)) method, the ink is first converted to a base64 encoded Ink Serialized Format byte array, and then the byte array is converted to a string to be written out to the XML file. The text data from the form is also written out to the XML file.


```C++
// Get the base64 encoded ISF
base64ISF_bytes = ic.Ink.Save(PersistenceFormat.Base64InkSerializedFormat);

// Convert it to a String
base64ISF_string = utf8.GetString(base64ISF_bytes);

// Write the ISF containing node to the XML
xwriter.WriteElementString("Ink", base64ISF_string);

// Write the text data from the form
// Note that the names are stored as XML fields, rather
// than custom properties, so that these properties can 
// be most easily accessible if the XML is saved in a database.
xwriter.WriteElementString("FirstName",FirstNameBox.Text);
xwriter.WriteElementString("LastName",LastNameBox.Text);
```



## Saving to an HTML File

The SaveHTML method uses the bounding box of the [Strokes](/previous-versions/ms827799(v=msdn.10)) collection to test for the presence of a signature. If the signature exists, it is converted to the fortified GIF format using the ink object's [Save](/previous-versions/dotnet/netframework-3.5/ms571335(v=vs.90)) method, and written to a file. The GIF is then referenced in the HTML file.


```C++
if (ic.Ink.Strokes.GetBoundingBox().IsEmpty)
{
   MessageBox.Show("Unable to save empty ink in HTML persistence format.");
}
else
{
    FileStream gifFile;
    byte[] fortifiedGif = null;
    ...

    // Create a directory to store the fortified GIF which also contains ISF
    // and open the file for writing
    Directory.CreateDirectory(nameBase + "_files");
    using (FileStream gifFile = File.OpenWrite(nameBase + "_files\\signature.gif"))
    {

        // Generate the fortified GIF represenation of the ink
        fortifiedGif = ic.Ink.Save(PersistenceFormat.Gif);

        // Write and close the gif file
        gifFile.Write(fortifiedGif, 0, fortifiedGif.Length);
    }
```



## Loading a File

The `OpenMenu_Click` method handles the Open dialog box, opens the file, and calls the loading method that corresponds to the user's choice.

## Loading an ISF File

The `LoadISF` method reads the previously created file and converts the Byte array to ink with the [Ink](/previous-versions/aa515768(v=msdn.10)) object's [Load](/previous-versions/ms569609(v=vs.100)) method. The ink collector is temporarily disabled to assign the Ink object to it. The `LoadISF` method then checks the Ink object's [ExtendedProperties](/previous-versions/ms582214(v=vs.100)) property for the first and last name strings.


```C++
Ink loadedInk = new Ink();
byte[] isfBytes = new byte[s.Length];

// read in the ISF
s.Read(isfBytes, 0, (int) s.Length);

// load the ink into a new ink object
// After an ink object has been "dirtied" it can never load ink again
loadedInk.Load(isfBytes);

// temporarily disable the ink collector and swap ink objects
ic.Enabled = false;
ic.Ink = loadedInk;
ic.Enabled = true;

// Repaint the inkable region
Signature.Invalidate();

ExtendedProperties inkProperties = ic.Ink.ExtendedProperties;

// Get the raw data out of this stroke's extended
// properties list, using the previously defined 
// Guid as a key to the extended property.
// Since the save method stored the first and last
// name information as extended properties, this
// information can be remove now that the load is complete.
if (inkProperties.DoesPropertyExist(FirstName))
{
    FirstNameBox.Text = (String) inkProperties[FirstName].Data;
    inkProperties.Remove(FirstName);
}
else
{
    FirstNameBox.Text = String.Empty;
}

if (inkProperties.DoesPropertyExist(LastName))
{
    LastNameBox.Text = (String) inkProperties[LastName].Data;
    inkProperties.Remove(LastName);
}
else
{
    LastNameBox.Text = String.Empty;
}
```



## Loading an XML File

The `LoadXML` method loads a previously created XML file, retrieves data from the Ink node, and converts the data in the node to ink using the [Ink](/previous-versions/aa515768(v=msdn.10)) object's [Load](/previous-versions/ms569609(v=vs.100)) method. The [InkCollector](/previous-versions/ms836493(v=msdn.10)) is temporarily disabled to assign the Ink object to it. The signature box is invalidated, and the first and last name information is retrieved from the XML document.


```C++
// This object encodes our byte data to a UTF8 string
UTF8Encoding utf8 = new UTF8Encoding();

XmlDocument xd = new XmlDocument();
XmlNodeList nodes;
Ink loadedInk = new Ink();

// Load the XML data into a DOM
xd.Load(s);

// Get the data in the ink node
nodes = xd.GetElementsByTagName("Ink");

// load the ink into a new ink object
// After an ink object has been "dirtied" it can never load ink again
if (0 != nodes.Count)
    loadedInk.Load(utf8.GetBytes(nodes[0].InnerXml));

// temporarily disable the ink collector and swap ink objects
ic.Enabled = false;
ic.Ink = loadedInk;
ic.Enabled = true;

// Repaint the inkable region
Signature.Invalidate();

// Get the data in the FirstName node
nodes = xd.GetElementsByTagName("FirstName");
if (0 != nodes.Count)
{
    FirstNameBox.Text = nodes[0].InnerXml;
}
else
{
    FirstNameBox.Text = String.Empty;
}

// Get the data in the LastName node
nodes = xd.GetElementsByTagName("LastName");
if (0 != nodes.Count)
{
    LastNameBox.Text = nodes[0].InnerXml;
}
else
{
    LastNameBox.Text = String.Empty;
}
```



## Closing the Form

The form's [Dispose](/dotnet/api/system.windows.forms.form.dispose?view=netcore-3.1&preserve-view=true) method disposes the [InkCollector](/previous-versions/ms836493(v=msdn.10)) object.

 

 
