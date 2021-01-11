---
description: The IFilter test suite validates your filter handlers.
ms.assetid: 5ee02af1-1dc9-4d21-868f-4c439970b1ba
title: Testing Filter Handlers
ms.topic: article
ms.date: 05/31/2018
---

# Testing Filter Handlers

The [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) test suite validates your filter handlers. The test suite does so by: calling [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) methods and checking the returned values for compliance with the **IFilter** interface specification; and checking that chunk identifiers are unique and increasing, that the **IFilter** interface behaves consistently after re-initialization, and that any **IFilter** method calls with invalid parameters return expected error codes. The test suite programs also dump the output of a file filtered by a filter handler, and check the **IFilter** registration information in the registry.

This topic is organized as follows:

- [Command-Line Invocation](#command-line-invocation)
  - [ifilttst.exe](#ifilttstexe)
  - [filtdump.exe](#filtdumpexe)
  - [filtreg.exe](#filtregexe)
  - [ifilttst.ini](#ifilttstini)
- [IFilter Test Procedure](#ifilter-test-procedure)
  - [Validation Test](#validation-test)
  - [Consistency Test](#consistency-test)
  - [Invalid Input Test](#invalid-input-test)
  - [Testing Different IFilter Configurations](#testing-different-ifilter-configurations)
- [Ensuring Registered Items Get Indexed](#ensuring-registered-items-get-indexed)
  - [Sample Log File](#sample-log-file)
  - [Sample Dump File](#sample-dump-file)
- [Additional Resources](#additional-resources)
- [Related topics](#related-topics)

> [!NOTE]  
> If a new filter handler for a file type is being installed as a replacement for an existing filter registration, the installer should save the current registration and restore it if the new filter handler is uninstalled. There is no mechanism to chain filters. Hence, the new filter handler is responsible for replicating any necessary functionality of the old filter.

## Command-Line Invocation

The [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) test suite consists of three command-line applications - [ifilttst.exe](#ifilttstexe), [filtdump.exe](#filtdumpexe), and [filtreg.exe](#filtregexe) and an initialization file, [ifilttst.ini](#ifilttstini).

> [!IMPORTANT]
> In Windows 7 and later, filters written in managed code are explicitly blocked. Filters MUST be written in native code due to potential common language runtime (CLR) versioning issues with the process that multiple add-ins run in.

### ifilttst.exe

The ifilttst.exe program runs several tests to validate a filter handler. The following example illustrates how to invoke the ifilttst.exe program from the command line:


```
ifilttst /i test.htm /l /d /v 1
```

The example performs the following tasks:

- Directs the program to filter the file test.htm
- Redirects the log messages to test.htm.log
- Redirects the dump messages to test.htm.dmp
- Sets the verbosity to 1

For the preceding command to work, three files must be located in the current working directory: `test.htm`, [ifilttst.exe](#ifilttstexe), and [ifilttst.ini](#ifilttstini). Command-line switches are listed in the following table.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Switch and possible variables</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>/i file name</strong></td>
<td>The input file or directory to be filtered. The file name can contain the wildcard characters <code>*</code> and <code>?</code>.</td>
</tr>
<tr class="even">
<td><strong>/l</strong></td>
<td>Log messages are directed to a file instead of the screen. Log messages describe the individual tests performed and the pass/fail results of the tests. The log file name is the same as the input file name but with a .log extension.</td>
</tr>
<tr class="odd">
<td><strong>/d</strong></td>
<td>Dump messages are directed to a file instead of the screen. Dump messages describe the contents of the chunks. The chunk structure is dumped when the verbosity level is 3. The dump file name is the same as the input file name but with a .dmp extension.</td>
</tr>
<tr class="even">
<td><strong>/-l</strong></td>
<td>Disable logging. This flag overrides the <code>/l</code> switch.</td>
</tr>
<tr class="odd">
<td><strong>/-d</strong></td>
<td>Disable dumping. This flag overrides the <code>/d</code> switch.</td>
</tr>
<tr class="even">
<td><strong>/v integer</strong></td>
<td>The verbosity level. The default is 3.
<ul>
<li>0 - The test logs only messages concerning specific <a href="https://www.bing.com/search?q=<strong>IFilter</strong>"><strong>IFilter</strong></a> interface failures. The test dumps the chunk contents.</li>
<li>1 - The test logs warning messages as well as those for level 0.</li>
<li>2 - The test logs messages concerning tests that passed as well as those for level 1.</li>
<li>3 - The test logs informational messages as well as those for level 2. In addition, the test dumps the structure of the chunk.</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>/t integer</strong></td>
<td>The number of threads to launch. The default is 1.</td>
</tr>
<tr class="even">
<td><strong>/r integer</strong>]</td>
<td>Recursively filters subdirectories. The optional integer parameter specifies the depth to which to exercise recursion. If no integer is specified, or if the integer is 0, full recursion is assumed. By default, the recursion depth is 1.</td>
</tr>
<tr class="odd">
<td><strong>/c integer</strong></td>
<td>The number of times to loop. If the integer is 0, the test loops infinitely. By default, the test loops only once.</td>
</tr>
</tbody>
</table>

> [!NOTE]  
> You must include a space between the command line switch and the value.

### filtdump.exe

The filtdump.exe program loads a filter handler for a specified document and prints the output produced by the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) DLL. The following example illustrates how to invoke the filtdump.exe program.

```
filtdump filename.ext
```
Filtdump.exe uses the [ILoadFilter::LoadIFilter](/windows/desktop/api/filtereg/nf-filtereg-iloadfilter-loadifilter) method to load the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) DLL appropriate for the specified file name extension and prints the results. For example, the following command instructs filtdump.exe to load the smpfilt.dll filter handler for the extension .smp, extract all text and properties from the file myfile.smp, and print the results.

```
filtdump myfile.smp
```

### filtreg.exe

The filtreg.exe program inspects [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) installation information in the registry. You invoke the filtreg.exe program from the command line by typing its name, as in the following example.

```
filtreg
```

Filtreg.exe enumerates all file name extensions that have filter handlers associated with them by printing the file name extension and the name of the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) DLL for the extension. This is a simple way to verify the correct installation of an **IFilter**.

### ifilttst.ini

An [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface is initialized by calling the [**IFilter::Init**](/windows/win32/api/filter/nf-filter-ifilter-init) method. The **IFilter::Init** method takes the following four parameters:

1. *grfFlags*
2. *cAttributes*
3. *aAttributes*
4. *pdwFlags*

The user of the ifilttst.exe program of the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) test suite can specify the values for these parameters in a file called ifilttst.ini. The following table describes the entries in the ifilttst.ini file that specify the first three parameters(the input parameters). For a sample file, see [Sample ifilttst.ini File](#sample-ifilttstini-file).

> [!NOTE]  
> There is no table entry for the *pdwFlags* parameter because it is an output parameter; it does not need to have any special value prior to the call to the [**IFilter::Init**](/windows/win32/api/filter/nf-filter-ifilter-init) method.

 | Entry         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Flags         | The names of the [**IFILTER\_INIT**](/previous-versions/windows/desktop/legacy/bb266511(v=vs.85)) flags that are to be joined by the OR operator to form the *grfFlags* parameter of the [**IFilter::Init**](/windows/win32/api/filter/nf-filter-ifilter-init) method. The flag names must all be uppercase, and on the same line.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| *cAttributes* | A decimal integer representing the value of the *cAttributes* parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| *aAttributes* | This entry must start with *aAttributes* and must be different from the other *aAttributes* entries within the section. Legal names for the *aAttributes* entry are: *aAttributes*, *aAttributes1*, *aAttributes2*, and so forth. The first token must be a GUID. The GUID must be formatted exactly as illustrated in the `[Test3]` section of the [Sample ifilttst.ini File](#sample-ifilttstini-file). The second token can be either a property identifier (PID) consisting of a number in hexadecimal notation, or a pointer to a wide character string (lpwstr). A lpwstr can be specified by enclosing the string in double quotes, as illustrated in the `[Test6]` section of the Sample ifilttst.ini File. |

If the Flags and *cAttributes* entries are not specified, they default to 0. If you set *cAttributes* equal to 2, you should specify two *aAttributes* names. In the `[Test5]` section of the sample, *cAttributes* is 1, but no *aAttributes* have been specified. The test then calls the [**IFilter::Init**](/windows/win32/api/filter/nf-filter-ifilter-init) method with *cAttributes* equal to 1 and *aAttributes* equal to **NULL**. This is a useful test case because it is likely to cause an access violation in the **IFilter::Init** method.

If ifilttst.exe cannot find a file named ifilttst.ini in the working directory, a default configuration is used to initialize the [**IFilter::Init**](/windows/win32/api/filter/nf-filter-ifilter-init) object. The following example illustrates the default configuration.

```
[default]
            grfFlags = IFILTER_INIT_APPLY_INDEX_ATTRIBUTES
            cAttributes = 0

```

### Sample ifilttst.ini File

The ifilttst.ini file is organized in sections, with the section name enclosed in square brackets. In the example, the sections are named `[Test1]`, `[Test2]`, and so forth. All section names must be unique. The test reads the values from the first section and initializes the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) with those values. Then all the tests are run using this **IFilter** configuration. Then the **IFilter** is released and reinitialized, using parameters that are listed above. The process is repeated until all configurations are tested.

```
; Only extract text from the object
            [Test1]
            Flags =
            cAttributes = 0

            // Get all attributes (text-type and internal value-type properties.
            [Test2]
            Flags = IFILTER_INIT_APPLY_INDEX_ATTRIBUTES
            cAttributes = 0

            // This also extracts just text from the object (the GUID is PSGUID_STORAGE, and the propid is
            // PID_STG_CONTENTS).
            [Test3]
            Flags = IFILTER_INIT_CANON_PARAGRAPHS IFILTER_INIT_HARD_LINE_BREAKS
            cAttributes = 1
            aAttributes1 = b725f130-47ef-101a-a5f1-02608c9eebac 13

            // Only extract requested attribute from the html object (the GUID corresponds to the HTML IFilter.
            [Test4]
            Flags = IFILTER_INIT_CANON_HYPHENS IFILTER_INIT_CANON_SPACES
            cAttributes = 1
            aAttributes1 = 70eb7a10-55d9-11cf-b75b-00aa0051fe20 2

            // Question: what happens if cAttributes is nonzero, but aAttributes is empty?
            [Test5]
            Flags = IFILTER_INIT_CANON_SPACES IFILTER_INIT_APPLY_INDEX_ATTRIBUTES IFILTER_INIT_APPLY_OTHER_ATTRIBUTES
            cAttributes = 1

            // Here is an attribute with a lpwstr instead of a propid (the lpwstr is enclosed in quotes).
            // The GUID corresponds to the meta tag clsid for the HTML IFilter.
            [Test6]
            Flags =
            cAttributes = 1
            aAttributes1 = D1B5D3F0-C0B3-11CF-9A92-00A0C908DBF1 "GENERATOR"
```

## IFilter Test Procedure

After the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) has been initialized, the ifilttst.exe program conducts a series of tests on the **IFilter**. In addition to following the **IFilter** test procedures, ensure that your **IFilter** implementation employs secure code practices. See "Secure Code Practices for Windows Search" in [Implementing Filter Handlers in Windows Search](-search-ifilter-constructing-filters.md).

### Validation Test

The validation test steps through the object one chunk at a time, verifying each individual chunk and all return codes. The validation test saves all returned [**STAT\_CHUNK**](/windows/win32/api/filter/ns-filter-stat_chunk) structures in a list.

The validation test verifies the following conditions:

- The [**STAT\_CHUNK**](/windows/win32/api/filter/ns-filter-stat_chunk).*idChunk* chunk IDs must be unique and increasing.
- The [**STAT\_CHUNK**](/windows/win32/api/filter/ns-filter-stat_chunk).*flags* parameter is a recognized chunk state, such as [**CHUNKSTATE**](/windows/win32/api/filter/ne-filter-chunkstate), CHUNK\_TEXT, or CenabledHUNK\_VALUE constants.
- The [**STAT\_CHUNK**](/windows/win32/api/filter/ns-filter-stat_chunk).*breakType* parameter is a recognized break type (0, 1, 2, 3, 4).
- If the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) initialization attributes specify that the **IFilter** should return only chunks containing internal value-type properties, then *idChunkSource* must equal 0.
- If the chunk is not derived that is, if it is not an internal value-type property, then [**STAT\_CHUNK**](/windows/win32/api/filter/ns-filter-stat_chunk).*idChunkSource* must equal **STAT\_CHUNK**.*idChunk*.
- [**IFilter::GetChunk**](/windows/win32/api/filter/nf-filter-ifilter-getchunk) returns S\_OK or other acceptable return value, such as FILTER\_E\_END\_OF\_CHUNKS, FILTER\_E\_LINK\_UNAVAILABLE, and so forth.
- If the chunk contains text, [**IFilter::GetText**](/windows/win32/api/filter/nf-filter-ifilter-gettext) returns S\_OK, FILTER\_S\_LAST\_TEXT, or FILTER\_E\_NO\_MORE\_TEXT.
- If [**IFilter::GetText**](/windows/win32/api/filter/nf-filter-ifilter-gettext) returns FILTER\_S\_LAST\_TEXT, the next call to **IFilter::GetText** returns FILTER\_E\_NO\_MORE\_TEXT.
- If the chunk contains a value, [**IFilter::GetValue**](/windows/win32/api/filter/nf-filter-ifilter-getvalue) returns S\_OK or FILTER\_E\_NO\_MORE\_VALUES.

### Consistency Test

The ifilttxt.exe program re-initializes the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface with the same parameters as in the validation test and performs a consistency test. If the **IFilter** implementation has been initialized with the [**IFILTER\_INIT**](/previous-versions/windows/desktop/legacy/bb266511(v=vs.85)) IFILTER\_INIT\_INDEXING\_ONLY flag, the test releases the **IFilter** interface and re-binds it before making another call to the [**IFilter::Init**](/windows/win32/api/filter/nf-filter-ifilter-init) method.

The consistency test verifies the following conditions:

- Each [**STAT\_CHUNK**](/windows/win32/api/filter/ns-filter-stat_chunk) structure returned by the [**IFilter::GetChunk**](/windows/win32/api/filter/nf-filter-ifilter-getchunk) method is identical to the corresponding **STAT\_CHUNK** returned in the validation test.
- [**IFilter::GetChunk**](/windows/win32/api/filter/nf-filter-ifilter-getchunk) returns S\_OK or other acceptable return value, such as FILTER\_E\_END\_OF\_CHUNKS, FILTER\_E\_LINK\_UNAVAILABLE, and so forth.

### Invalid Input Test

The ifilttst.exe program re-initializes the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface with the same parameters,and performs an invalid input test. This test steps through the document one chunk at a time making function calls incorrectly, such as calling the [**IFilter::GetValue**](/windows/win32/api/filter/nf-filter-ifilter-getvalue) method when the current chuck contains text. The test checks all return codes for compliance with the **IFilter** specification.

The invalid input test verifies the following conditions:

- If the current chunk contains text, [**IFilter::GetValue**](/windows/win32/api/filter/nf-filter-ifilter-getvalue) returns FILTER\_E\_NO\_VALUES, and a call to [**IFilter::GetText**](/windows/win32/api/filter/nf-filter-ifilter-gettext) succeeds.
- If the current chunk contains a value, [**IFilter::GetText**](/windows/win32/api/filter/nf-filter-ifilter-gettext) returns FILTER\_E\_NO\_TEXT, and a call to [**IFilter::GetValue**](/windows/win32/api/filter/nf-filter-ifilter-getvalue) succeeds.
- If the previous call to [**IFilter::GetText**](/windows/win32/api/filter/nf-filter-ifilter-gettext) returned FILTER\_E\_NO\_MORE\_TEXT, successive calls to **IFilter::GetText** return FILTER\_E\_NO\_MORE\_TEXT.
- If the previous call to [**IFilter::GetValue**](/windows/win32/api/filter/nf-filter-ifilter-getvalue) returned FILTER\_E\_NO\_MORE\_VALUES, successive calls to **IFilter::GetValue** return FILTER\_E\_NO\_MORE\_VALUES.
- If the previous call to [**IFilter::GetChunk**](/windows/win32/api/filter/nf-filter-ifilter-getchunk) returned FILTER\_E\_END\_OF\_CHUNKS, successive calls to **IFilter::GetChunk** return FILTER\_E\_END\_OF\_CHUNKS.

> [!NOTE]  
> The invalid input test compares the current chunk structures to those returned in the validation test to make sure they are identical.

### Testing Different IFilter Configurations

The ifilttst.exe program releases the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface and rebinds, this time initializing it with the next set of parameters. The test repeats the cycle: validation test, consistency test, and invalid input test, until all the desired **IFilter** configurations specified in [ifilttst.ini](#ifilttstini) file have been tested.

## Ensuring Registered Items Get Indexed

The final test of your [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) ensures that your **IFilter** is properly registered and that it is invoked to index the items that you registered to use it. You can use the Catalog Manager to initiate re-indexing, or use the Crawl Scope Manager (CSM) to set up default rules indicating the URLs that you want the indexer to crawl. After indexing is complete, use the Windows Search UI to search for a string in the content or properties of items. If the items were indexed, they will appear in the search results.

For more information about re-indexing, see [Using the Catalog Manager](-search-3x-wds-mngidx-catalog-manager.md) and [Using the Crawl Scope Manager](-search-3x-wds-extidx-csm.md). The ReindexMatchingUrls code sample demonstrates ways to specify which files to re-index and how. The CrawlScopeCommandLine code sample demonstrates how to define command line options for Crawl Scope Manager (CSM) indexing operations. Both code samples are available on [GitHub](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/WindowsSearch).

### Sample Log File

Upon request, the Ifilttst.exe program can produce a log containing a description of the steps it takes during execution. The following examples are excerpts from a log file, with the verbosity set to the highest possible value 3.

```
            1. INFO----**** New configuration ****
            2.
            3. Section name : Test2
            4. grfFlags     : 63
            5. cAttributes  : 0
            6. aAttributes  : NONE
            7. pdwFlags     : 0
            8.
            9. INFO----Successfully bound filter.
            10.
            11. PASS----Init() returned a valid value for pdwFlags.
            12.
            13. INFO----Successfully initialized filter.
            14.
            15. INFO----Performing validation test. In this part of the test, the chunks structures
            16.         returned by the IFilter are checked for correctness, and the return values
            17.         of the IFilter calls are checked.
            18.
            19. PASS----GetChunk() succeeded.
            20.
            21. PASS----The current chunk has a legal value for the flags field.

```

The first line is an informational message, indicating that a new configuration has been loaded from the ifilttst.ini file. Line (3) indicates the section name in the ifilttst.ini file from which the current configuration has been read. Lines (4) through (7) list the parameters to [**IFilter::Init**](/windows/win32/api/filter/nf-filter-ifilter-init). The lines starting with `INFO` are informational messages about the binding of the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) and the start of the validation test. Lines starting with `PASS` are messages regarding specific tests that have passed.

The line in the following log example is a warning. Warnings call attention to [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) behavior that is problematic, although legal. This warning indicates that the [**IFilter::GetChunk**](/windows/win32/api/filter/nf-filter-ifilter-getchunk) method has returned a text chunk that contains no text.

```
WARNING-First call to GetText() returned FILTER_E_NO_MORE_TEXT.
```

The following example error message indicates that the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) emitted a chunk that was not requested.

```
            ERROR---The IFilter has emitted a chunk which it was not requested to emit.
            Check the initialization parameters in section Test1 of the initialization file.
            INFO----Current chunk propid : 0x5
```

In the case of this example error message, the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) emitted a chunk with a PID of `0x5`. Inspection of section `[Test1]` in ifilttst.ini would show that the **IFilter** was configured to not emit chunks with this PID. For example, if neither IFILTER\_INIT\_APPLY\_INDEX\_ATTRIBUTES nor IFILTER\_INIT\_APPLY\_OTHER\_ATTRIBUTES were specified in the Flags entry and if *cAttributes* were 0, then **IFilter** would emit only chunks with a PID of `0x13` and corresponding to PID\_STG\_CONTENTS.

### Sample Dump File

Upon request, the Ifilttst.exe program can produce a dump containing the chunks it finds and their content. The following example is an excerpt from such a dump file.

```
                1. Chunk ID: ........... 2
                2. Chunk Break Type: ... END OF SENTENCE
                3. Chunk State: ........ TEXT
                4. Chunk Locale: ....... 0x411
                5. Chunk Source ID: .... 2
                6. Chunk Start Source .. 0x0
                7. Chunk Length Source . 0x0
                8. GUID ................ b725f130-47ef-101a-a5f1-02608c9eebac
                9. Property ID ......... 0x13

                10. This is a HTML IFilter test page

                11. Chunk ID: ........... 3
                12. Chunk Break Type: ... END OF SENTENCE
                13. Chunk State: ........ TEXT
                14. Chunk Locale: ....... 0x411
                15. Chunk Source ID: .... 2
                16. Chunk Start Source .. 0x0
                17. Chunk Length Source . 0x0
                18. GUID ................ f29f85e0-4ff9-1068-ab91-08002b27b3d9
                19. Property ID ......... 0x2

                20. This is a HTML IFilter test page

                21. Chunk ID: ........... 4
                22. Chunk Break Type: ... END OF SENTENCE
                23. Chunk State: ........ VALUE
                24. Chunk Locale: ....... 0x411
                25. Chunk Source ID: .... 2
                26. Chunk Start Source .. 0x0
                27. Chunk Length Source . 0x0
                28. GUID ................ f29f85e0-4ff9-1068-ab91-08002b27b3d9
                29. Property ID ......... 0x2

                30. This is an HTML IFilter test page
```

The first nine lines describe the current chunk structure. The GUID and the PID correspond to PSGUID\_STORAGE / PID\_STG\_CONTENTS. This is a chunk containing plain text. The text is in the following chunk structure:

```
10. This is an HTML IFilter test page
```

The next chunk, starting at line 11, has a different GUID, corresponding to the `HTML IFilter`, and a different PID, corresponding to an HTML HREF. This is an internal value-type property, exported by the `HTML IFilter`.

The next chunk, starting at line 21, has the same GUID and PID, but its chunk state is `VALUE` instead of `TEXT`. Note that the text in these last two chunks is the same as for the first chunk. But because the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) is designed for three attributes (plain text, HTML HREF as text, and HTML HREF as a value) to be applied to this phrase, the results are emitted in three separate chunks.

## Additional Resources

- The [IFilterSample](-search-sample-ifiltersample.md) code sample, available on [GitHub](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/WindowsSearch/IFilterSample), demonstrates how to create an IFilter base class for implementing the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface.
- For an overview of the indexing process, see [The Indexing Process](-search-indexing-process-overview.md).
- For an overview of file types, see [File Types](../shell/fa-file-types.md).
- To query file association attributes for a file type, see [PerceivedTypes, SystemFileAssociations, and Application Registration](/previous-versions/windows/desktop/legacy/cc144150(v=vs.85)).

## Related topics

[Developing Filter Handlers](-search-ifilter-conceptual.md)

[About Filter Handlers in Windows Search](-search-ifilter-about.md)

[Best Practices for Creating Filter Handlers in Windows Search](-search-3x-wds-extidx-filters.md)

[Returning Properties from a Filter Handler](-search-ifilter-property-filtering.md)

[Filter Handlers that Ship with Windows](-search-ifilter-implementations.md)

[Implementing Filter Handlers in Windows Search](-search-ifilter-constructing-filters.md)

[Registering Filter Handlers](-search-ifilter-registering-filters.md)
