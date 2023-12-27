import VideoDownloads from "./VideoDownloads.jsx";

export default () => {
    const link = "https://www.youtube.com/embed/zpOULjyy-n8?rel=0";

    return (
        <>
            <section className="p-5 container text-center">
                <div>
                    <h1>Insira um link abaixo para download</h1>
                </div>
                <div>
                    <div className="input-group pt-5 pb-3">
                        <input type="text" className="form-control" />
                        <button className="btn btn-primary">enviar</button>
                    </div>
                    <div>
                        <p>pequeno texto</p>
                    </div>
                </div>
            </section>
            <VideoDownloads link={link} />
        </>
    );
};
