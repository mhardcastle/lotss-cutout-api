import requests
import sys

def get_cutout(outfile,pos,size=30,low=False):
    '''
    Get a cutout at position pos with size size arcmin. If low is
    True, get the 20-arcsec cutout, else get the 6-arcsec one. Save to
    outfile.

    '''

    url='https://lofar-surveys.org/'
    if low:
        page='dr2-low-cutout.fits'
    else:
        page='dr2-cutout.fits'
    r=requests.get(url+page,params={'pos':pos,'size':size})
    with open(outfile,'wb') as o:
        o.write(r.content)
    r.close()

if __name__=='__main__':
    # Example code using a list of target names supplied on the command line
    infile=sys.argv[1]
    objects=[l.rstrip() for l in open(infile).readlines()]
    for oname in objects:
        print('Downloading image for',oname)
        get_cutout(oname+'.fits',oname,low=True)
