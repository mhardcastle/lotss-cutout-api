import requests
import sys

def get_cutout(outfile,pos,size=30,low=False,dr3=False,verbose=False,auth=None):
    '''Get a cutout at position pos with size size arcmin. If low is
    True, get the 20-arcsec cutout, else get the 6-arcsec one. If dr3
    is true, try to access the DR3 data instead. Save to outfile.

    '''
    base='dr3' if dr3 else 'dr2'
    url='https://lofar-surveys.org/'
    if low:
        page=base+'-low-cutout.fits'
    else:
        page=base+'-cutout.fits'
    
    if verbose:
        print('Trying',url+page,'params=',{'pos':pos,'size':size})
    r=requests.get(url+page,params={'pos':pos,'size':size},auth=auth,stream=True)
    if verbose:
        print('received response code',r.status_code,'and content type',r.headers['content-type'])
    if r.status_code!=200:
        raise RuntimeError('Status code %i returned' % r.status_code)
    if r.headers['content-type']!='application/fits':
        raise RuntimeError('Server did not return FITS file, probably no coverage of this area')

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
