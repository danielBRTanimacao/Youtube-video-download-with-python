export default function SectionPrincipal() {
    return (
        <>
            <section className="bg-black-2 text-light p-5">
                <div className="container text-center">
                    <div>
                        <h1>texto area</h1>
                    </div>
                    <div className="input-group">
                        <input
                            type="text"
                            className="form-control"
                            placeholder="Link do vídeo"
                            aria-describedby="send-link"
                        />
                        <button
                            className="btn btn-outline-warning"
                            type="button"
                            id="send-link"
                        >
                            Enviar link
                        </button>
                    </div>
                    <div>
                        <p>download area</p>
                    </div>
                </div>
            </section>
        </>
    );
}
