using UnityEngine;

public class Drag : MonoBehaviour
{
    private Vector3 startPosition; // Posição inicial do personagem
    private Vector3 dragPosition; // Posição durante o arraste
    private bool isDragging = false; // Controle de arraste
    private Rigidbody2D rb;

    public float releaseForce = 5f; // Força ao soltar o elástico

    void Start()
    {
        rb = GetComponent<Rigidbody2D>(); // Obtém o Rigidbody2D do personagem
        startPosition = transform.position; // Define a posição inicial
    }

    void OnMouseDown()
    {
        isDragging = true; // Inicia o arraste
        rb.isKinematic = true; // Desativa a física temporariamente
    }

    void OnMouseDrag()
    {
        dragPosition = Camera.main.ScreenToWorldPoint(Input.mousePosition); // Converte a posição do mouse
        dragPosition.z = 0; // Mantém no mesmo plano
        transform.position = dragPosition; // Move o personagem
    }

    void OnMouseUp()
    {
        isDragging = false; // Termina o arraste
        rb.isKinematic = false; // Reativa a física
        Vector2 force = (startPosition - transform.position) * releaseForce; // Calcula a força
        rb.AddForce(force, ForceMode2D.Impulse); // Aplica a força de impulso
        Invoke("ResetPosition", 2f); // Reseta a posição após 2 segundos
    }

    void ResetPosition()
    {
        rb.velocity = Vector2.zero; // Para o movimento
        transform.position = startPosition; // Volta à posição inicial
    }
}

