from ninja import Router

router = Router()

@router.post("/")
def create(request):
    return True

@router.get("/{id}")
def get_one(request, id):
    return True

@router.get("/")
def list(request):
    return True

@router.delete("/{id}")
def remove(request, id):
    return True

@router.patch("/{id}")
def update(request, id):
    return True