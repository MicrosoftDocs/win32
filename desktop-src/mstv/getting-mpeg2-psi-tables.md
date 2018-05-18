---
title: Getting MPEG-2 PSI Tables
description: Getting MPEG-2 PSI Tables
ms.assetid: 'e75ef5c2-7316-4f23-b108-ff16cd97622f'
---

# Getting MPEG-2 PSI Tables

The [**MPEG-2 Sections and Tables**](mpeg-2-sections-and-tables-filter.md) filter retrieves Program Specific Information (PSI) tables from an MPEG-2 transport stream. You can use this filter to obtain any kind of PSI data, such as ATSC Program and System Information Protocol (PSIP) tables, DVB service information (SI), conditional access tables (CATs), DSM-CC messages, or private table data.

To use this filter, connect it to the [MPEG-2 Demultiplexer](https://msdn.microsoft.com/library/windows/desktop/dd390715) ("demux"). In a digital television graph, the filter is connected to pin 5 on the demux by default. For other kinds of filter graph, the application should create a new output pin on the demux and connect it to the filter. Create the output pin by calling the [**IMpeg2Demultiplexer::CreateOutputPin**](https://msdn.microsoft.com/library/windows/desktop/dd407129) method on the demux. Set the major type to MEDIATYPE\_MPEG2\_SECTIONS and the subtype to MEDIASUBTYPE\_MPEG2DATA.

To get PSI tables from the transport stream, use the [**IMpeg2Data**](impeg2data.md) interface on the filter. If you already have a pointer to the filter from building the graph, call **QueryInterface** to get the interface pointer. Otherwise, use [**IFilterGraph::EnumFilters**](https://msdn.microsoft.com/library/windows/desktop/dd390019) to enumerate the filters in the graph, and then query each filter for the interface. (See the example code in [Find an Interface on a Filter or Pin](https://msdn.microsoft.com/library/windows/desktop/dd375791).) For digital television applications, if your application uses the Video Control to build the graph, call the [**IMSVidGraphSegmentContainer::get\_Graph**](imsvidgraphsegmentcontainer-get-graph.md) method to get a pointer to the filter graph.

The application can retrieve a single table section, a complete table, or a continuous stream of table sections.

### Get a Section or Complete Table

To get one section from a table, call the [**IMpeg2Data::GetSection**](impeg2data-getsection.md) method:


```C++
#include <mpeg2data.h>

IMpeg2Data *pMPEG = NULL; // Pointer to the Sections and Tables filter.
ISectionList *pSectionList = NULL;

// Initialize pMPEG by searching the graph for a filter that exposes the
// IMpeg2Data interface (not shown). Run the graph to get MPEG-2 data.

// Get the next section with PID 0, which is reserved for the PAT.
PID pid = 0x00;
TID tid = 0x00;
DWORD dwTimeout = 5000; // msec

hr = pMPEG->GetSection(pid, tid, NULL, dwTimeout, &amp;pSectionList);
if (SUCCEEDED(hr))
{
    // Use pSectionList to access the data
    pSectionList->Release();
}
```



The first two parameters of [**GetSection**](impeg2data-getsection.md) specify a packet identifier (PID) and a table identifier (TID). The method blocks until the filter receives a section that matches these values or the method times out, whichever happens first. Note that you do not have to map the PID on the demux filter; the **GetSection** method automatically does this. The third parameter is an optional pointer to an [**MPEG2\_FILTER**](mpeg2-filter.md) structure; this can be used to specify additional fields to match, such as the version number or the current/next indicator. The [**GetSection**](isectionlist-getsectiondata.md) method returns a pointer to the [**ISectionList**](isectionlist.md) interface, which is used to get the section data.

To get a complete table, call the [**IMpeg2Data::GetTable**](impeg2data-gettable.md) method. This method has the same semantics as the [**GetSection**](impeg2data-getsection.md) method. However, it blocks until the filter has accumulated a complete table (or the method times out). If the method succeeds, the [**ISectionList**](isectionlist.md) interface references a list of all the sections in the table, rather than one section.

Use the [**ISectionList**](isectionlist.md) interface to access the section data. Call [**ISectionList::GetNumberOfSections**](isectionlist-getnumberofsections.md) to find how many sections were captured. Then call [**ISectionList::GetSectionData**](isectionlist-getsectiondata.md) to get data from each section:


```C++
hr = pMPEG->GetTable(pid, tid, NULL, dwTimeout, &amp;pSectionList);
if (SUCCEEDED(hr))
{
    WORD cSections;
    hr = pSectionList->GetNumberOfSections(&amp;cSections);
    for (WORD i = 0; i < cSections; i++)
    {
        // Iterate through the list of sections.
        SECTION *pSection;
        DWORD cbSize;
        hr = pSectionList->GetSectionData(i, &amp;cbSize, &amp;pSection);
        if (SUCCEEDED(hr))
        {
            // Examine the data contained in pSection.
        }
    }
    pSectionList->Release();
}
```



The [**GetSectionData**](isectionlist-getsectiondata.md) method returns the data as a [**SECTION**](section.md) structure. This structure contains the section header fields, plus a pointer to the rest of the data. If the section\_syntax\_indicator bit in the header is set to 1, it means the section contains extended header information. You can get the extended header fields by casting the **SECTION** structure to a [**LONG\_SECTION**](long-section.md) type. For DSM-CC messages, you can cast the **SECTION** structure to a [**DSMCC\_SECTION**](dsmcc-section.md) structure.

The following code is a function that displays section data in the debugger window. This function shows how to access all of the header fields; for the remaining data, it displays the raw byte values.


```C++
#include <mpeg2data.h>
#include <mpeg2bits.h>

void PrintByteArray(const BYTE *pData, long cbSize); // Forward declare.

HRESULT PrintMpeg2Section(SECTION *pSection, DWORD dwPacketLength)
{
    if (!pSection)
    {
        return E_POINTER;
    }
    if (dwPacketLength < sizeof(SECTION))
    {
        ATLTRACE(L"Malformed MPEG-2 section data.\n");
        return E_FAIL;
    }

    // Coerce the header bits to a bit field structure.
    MPEG_HEADER_BITS *pHeader = (MPEG_HEADER_BITS*)&amp;pSection->Header.W;

    ATLTRACE(L"Packet Length: %d bytes.\n", dwPacketLength);
    ATLTRACE(L"Table ID: 0x%.2x\n", pSection->TableId);
    ATLTRACE(L"Section Syntax Indicator: 0x%x\n", 
        pHeader->SectionSyntaxIndicator);
    ATLTRACE(L"Private Indicator: 0x%x\n", pHeader->PrivateIndicator);
    ATLTRACE(L"Reserved: 0x%x\n", pHeader->Reserved);
    ATLTRACE(L"Section Length: %d\n", pHeader->SectionLength);

    if (pHeader->SectionSyntaxIndicator)
    {
        // Coerce the section structure to a long section header.
        LONG_SECTION *pLong = (LONG_SECTION*) pSection;

        MPEG_HEADER_VERSION_BITS *pVersion = 
            (MPEG_HEADER_VERSION_BITS*)&amp;pLong->Version.B;

        ATLTRACE(L"Long section fields ...\n");
        ATLTRACE(L"TID Extension: 0x%.4x\n", pLong->TableIdExtension);
        ATLTRACE(L"Reserved: 0x%x\n", pVersion->Reserved);
        ATLTRACE(L"Version: %d\n", pVersion->VersionNumber);
        ATLTRACE(L"Current/Next: 0x%x\n", pVersion->CurrentNextIndicator);
        ATLTRACE(L"Section Number: %d\n", pLong->SectionNumber);
        ATLTRACE(L"Last Section Number: %d\n", pLong->LastSectionNumber);

        // Look for DSM-CC message types.
        if (pSection->TableId == 0x3B || pSection->TableId == 0x3C)
        {
            // Coerce the section structure to a DSM-CC header.
            DSMCC_SECTION *pDsmcc = (DSMCC_SECTION*) pSection;

            ATLTRACE(L"DSM-CC section fields ...\n");
            ATLTRACE(L"Protocol Discriminator: 0x%.2x\n", 
                pDsmcc->ProtocolDiscriminator);
            ATLTRACE(L"Type: 0x%.2x\n", pDsmcc->DsmccType);
            ATLTRACE(L"MessageId: 0x%.4x\n", pDsmcc->MessageId);
            ATLTRACE(L"TransactionId: 0x%.8x\n", pDsmcc->TransactionId);
            ATLTRACE(L"Reserved: 0x%.2x\n", pDsmcc->Reserved);
            ATLTRACE(L"AdaptationLength: 0x%.2x\n", 
                pDsmcc->AdaptationLength);
            ATLTRACE(L"MessageLength: 0x%.4x\n", pDsmcc->MessageLength);
            ATLTRACE(L"Remaining bytes ...\n");
            PrintByteArray(pDsmcc->RemainingData, 
                pDsmcc->MessageLength + pDsmcc->AdaptationLength);
        }
        else
        {
            // This is not a DSM-CC message. Print the remaining bytes.
            ATLTRACE(L"Remaining bytes ...\n");
            PrintByteArray(pLong->RemainingData, pHeader->SectionLength - 5);
        }
    }
    else
    {
        // Not a long section header. Print the remaining bytes.
        ATLTRACE(L"Section bytes ...\n");
        PrintByteArray(pSection->SectionData, pHeader->SectionLength);
    }

    return S_OK;
}

void PrintByteArray(const BYTE *pData, long cbSize)
{
    for (int iter = 0; iter < cbSize; iter++)
    {
        ATLTRACE(L"0x%.2x ", pData[iter]);
        if (iter % 8 == 7)
        {
            ATLTRACE(L"\n");
        }
    }
}
```



Note that some of the header information is packed into bit fields. Within the header structures, these fields are defined as simple byte and **WORD** types. To get the individual bit fields, you must coerce some of the structure members, as shown in the example. For example, the **Header.W** member of the [**SECTION**](section.md) structure can be cast to an [**MPEG\_HEADER\_BITS**](mpeg-header-bits.md) structure.

The data that follows the header is returned as an unparsed byte array. It is up to the client to parse the data. Therefore, you must understand the format of the transport stream that you expect to receive. Often, this will depend on the network standard in use. For example, ATSC and DVB use different specifications for service information tables. Typically you will need to apply bit masks to get some of the fields, and convert the data from network byte order to host byte order.

### Get a Stream of Sections

Instead of making synchronous requests for one section or one table at a time, you can use the [**IMpeg2Data::GetStreamOfSections**](impeg2data-getstreamofsections.md) method to get a continuous stream of sections. The **GetStreamOfSections** method returns immediately, and the caller provides an event which is signaled whenever new data arrives. Start by creating the event, and then call **GetStreamOfSections** with the PID and TID values to match against:


```C++
HANDLE hCompleted = CreateEvent(NULL, FALSE, FALSE, NULL);
if (!hCompleted) 
{
    // The event was not created. Handle the error.
}
IMpeg2Stream *pStream = 0;
hr = pMPEG->GetStreamOfSections(pid, tid, NULL, hCompleted, &amp;pStream);
```



If successful, the method returns an [**IMpeg2Stream**](impeg2stream.md) interface pointer. Use this interface to get the section data.

Allocate one or more buffers to hold the data. Each buffer must be 4096 bytes or larger. Also declare an [**MPEG\_STREAM\_BUFFER**](mpeg-stream-buffer.md) structure to manage the buffers. For each section that you retrieve, set the **pDataBuffer** member of the structure to point to a buffer, and set **dwDataBufferSize** equal to the size of the buffer. Set the other members to zero:


```C++
const int cBufferSize = 4096; // Buffer size.
BYTE Buffer1[cBufferSize];    // The buffer.
MPEG_STREAM_BUFFER streamBuffer;  // Structure to manage the buffer(s).

ZeroMemory(&amp;streamBuffer, sizeof(MPEG_STREAM_BUFFER));
streamBuffer.dwDataBufferSize = cBufferSize;
streamBuffer.pDataBuffer = (BYTE*)Buffer1;
```



Call [**IMpeg2Stream::SupplyDataBuffer**](impeg2stream-supplydatabuffer.md) and wait for the event to be signaled. When the event is signaled, examine the **hr** field in the [**MPEG\_STREAM\_BUFFER**](mpeg-stream-buffer.md) structure. If this field contains a success code, it means the request was successful and the buffer contains one section. The **dwSizeOfDataRead** field specifies the size of the section data. The data is unparsed, in network byte order.


```C++
hr = pStream->SupplyDataBuffer(&amp;streamBuffer);
if (SUCCEEDED(hr))
{
    DWORD dwWait = WaitForSingleObject(hRequestCompleted, dwTimeout);
    if (dwWait == WAIT_OBJECT_0)
    {
        if (SUCCEEDED(streamBuffer.hr))
        {
            // Buffer1 contains section data.
        }
    }
}
```



## Related topics

<dl> <dt>

[Microsoft TV Technologies](microsoft-tv-technologies-portal.md)
</dt> </dl>

 

 




