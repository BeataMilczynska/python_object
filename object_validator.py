
#obiekty nie mogą wychodzić poza width i height, czyli spełniać warunki:
#ymin and ymax <= weidth
#xmin and xmax <= height

def object_validator(xmlstr):
height_min
height_max
weidth_min
weidth_max
#tu się zastanawiam czy sięe nie odwłać do size po prostu bo tam są wymiary obrazka
#ale na razie rozdzielam osobno

object
size
    if (xmin <= height_min and xmax <=height_max):
        print("OK")
    else:
        print("Objekt wykracza poza wysokość")

    if (ymin <= weidth_min and ymax <= weidth_max):
        print("OK")
    else:
        print("Objekt wykracza poza szerokość")

#na poniższym przykładzie mam jeszcze pomysł by była funkcja która porównuje wszystkie
#bandbox z size
#   <<annotation>
	<folder>VOC2012</folder>
	<filename>2007_000027.jpg</filename>
	<source>
		<database>The VOC2007 Database</database>
		<annotation>PASCAL VOC2007</annotation>
		<image>flickr</image>
	</source>
	<size>
		<width>486</width>
		<height>500</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>person</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>174</xmin>
			<ymin>101</ymin>
			<xmax>349</xmax>
			<ymax>351</ymax>
		</bndbox>
		<part>
			<name>head</name>
			<bndbox>
				<xmin>169</xmin>
				<ymin>104</ymin>
				<xmax>209</xmax>
				<ymax>146</ymax>
			</bndbox>
		</part>
		<part>
			<name>hand</name>
			<bndbox>
				<xmin>278</xmin>
				<ymin>210</ymin>
				<xmax>297</xmax>
				<ymax>233</ymax>
			</bndbox>
		</part>
		<part>
			<name>foot</name>
			<bndbox>
				<xmin>273</xmin>
				<ymin>333</ymin>
				<xmax>297</xmax>
				<ymax>354</ymax>
			</bndbox>
		</part>
		<part>
			<name>foot</name>
			<bndbox>
				<xmin>319</xmin>
				<ymin>307</ymin>
				<xmax>340</xmax>
				<ymax>326</ymax>
			</bndbox>
		</part>
	</object>
</annotation>